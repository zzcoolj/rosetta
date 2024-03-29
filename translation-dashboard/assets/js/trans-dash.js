var target_lang = getQueryVariable("target_lang");
console.log("target language: " + target_lang);

var margin = { top: 50, right: 0, bottom: 100, left: 30 },
        width = 960 - margin.left - margin.right,
        height = 1800 - margin.top - margin.bottom, // legend y position control
        gridSize = Math.floor(width / 24),
        legendElementWidth = gridSize*2,
        buckets = 9,
        colors = ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"], // alternatively colorbrewer.YlGnBu[9]
        // TODO Make days and times automatically created based on the all-para-count file
        days = Array.from(Array(44).keys()).slice(1), // All translated versions have 43 chapters, 'slice' is for starting from 1 not 0
        times = ['en', 'ba', 'bu', 'du', 'fi', 'ge', 'hu', 'pol', 'por', 'ru', 'uk'];
    // datasets = ["../data/data.tsv", "../data/data2.tsv"];
    datasets = ["data/para-count-heatmap/all-para-count.tsv"];

    var svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // selectAll is just in case these labels already exist. In that case, it updates the corresponding information.
    var dayLabels = svg.selectAll(".dayLabel")
        .data(days)
        .enter().append("text")
        .text(function (d) { return d; })
        .attr("x", 0)
        .attr("y", function (d, i) { return i * gridSize; })
        .style("text-anchor", "end")
        .attr("transform", "translate(-6," + gridSize / 1.5 + ")")
        .attr("class", function (d, i) { return ((i >= 0 && i <= 4) ? "dayLabel mono axis axis-workweek" : "dayLabel mono axis"); })
        .attr("id", function(d) {return d;})
        .on("click", chapterLabelOnClick)
        // .on({
        //     "mouseover": function(d) {
        //         d3.select(this).style("cursor", "pointer");
        //     },
        //     "mouseout": function(d) {
        //         d3.select(this).style("cursor", "default");
        //     }
        // })
    ;

    var timeLabels = svg.selectAll(".timeLabel")
        .data(times)
        .enter().append("text")
        .text(function(d) { return d; })
        .attr("x", function(d, i) { return i * gridSize; })
        .attr("y", 0)
        .style("text-anchor", "middle")
        .attr("transform", "translate(" + gridSize / 2 + ", -6)")
        .attr("class", function(d, i) { return ((i >= 7 && i <= 16) ? "timeLabel mono axis axis-worktime" : "timeLabel mono axis"); })
        .attr("id", function(d) {return d;})
        .on("click", textLabelOnClick)
        .on({
            "mouseover": function(d) {
                d3.select(this).style("cursor", "pointer");
            },
            "mouseout": function(d) {
                d3.select(this).style("cursor", "default");
            }
        })
    ;

    // Drawing cells
    var heatmapChart = function(tsvFile) {
        d3.tsv(tsvFile,
            function(d) {
                // Accessor function to tsvFile, convert string to numbers during the loading of the data.
                return {
                    day: +d.day,
                    hour: +d.hour,
                    value: +d.value,
                };
            },
            function(error, data) {
                // Quantile scales map a sampled input domain to a discrete range.
                var colorScale = d3.scale.quantile()
                    // .domain([0, buckets - 1, d3.max(data, function (d) { return d.value; })])
                    .domain([0, 1, 2, 3, 5, 10, 20, 30, 40, d3.max(data, function (d) { return Math.abs(d.value - data[d.day-1].value); })])
                    .range(colors);
                //TODO domain array automatic generation
                // console.log(colorScale.quantiles())
                // console.log(colorScale(0))
                // console.log(colorScale(1))
                // console.log(colorScale(2))
                // console.log(colorScale(3))
                // console.log(colorScale(6))
                // console.log(colorScale(15))
                // console.log(colorScale(25))
                // console.log(colorScale(33))
                // console.log(colorScale(42))

                var cards = svg.selectAll(".hour")
                    .data(data, function(d) {return d.day+':'+d.hour;});

                cards.enter().append("rect")
                    .attr("x", function(d) { return (d.hour - 1) * gridSize; })
                    .attr("y", function(d) { return (d.day - 1) * gridSize; })
                    .attr("rx", 4)
                    .attr("ry", 4)
                    .attr("class", "hour bordered")
                    .attr("width", gridSize)
                    .attr("height", gridSize)
                    .style("fill", colors[0]);

                /*
                Fill color when launching the page
                Color depends on the difference of # paragraphs compared with English version (data[0]~data[42])
                */
                cards.transition().duration(1000)
                    // .style("fill", function(d) { return colorScale(d.value); });
                    .style("fill", function(d) { return colorScale(Math.abs(d.value - data[d.day-1].value)); });

                cards.append("title");
                cards.select("title").text(function(d) { return d.value; });

                /*
                Coding tips: .enter is usually followed by .append which adds elements to the DOM.
                Here we are joining cards array to an empty selection (which is a very common pattern in the examples
                on the D3 website. ref: https://d3indepth.com/enterexit/)
                 */
                cards.enter().append("text")
                    .text(function(d) { return d.value; })
                    .on("click", cellOnClick)
                    .on({
                        "mouseover": function(d) {
                            if(d.hour == 2){
                                d3.select(this).style("cursor", "pointer");
                            }
                        },
                        "mouseout": function(d) {
                            d3.select(this).style("cursor", "default");
                        }
                    })
                    .attr("class", "mono")
                    .attr("x", function(d) { return (d.hour - 0.5) * gridSize; })
                    .attr("y", function(d) { return (d.day - 0.35) * gridSize; })
                    .attr("font-weight", "bold")
                    .style('fill', 'FireBrick')
                    .style("text-anchor", "middle");

                cards.exit().remove();


                var legend = svg.selectAll(".legend")
                    .data([0].concat(colorScale.quantiles()), function(d) { return d; });

                legend.enter().append("g")
                    .attr("class", "legend");

                legend.append("rect")
                    .attr("x", function(d, i) { return legendElementWidth * i; })
                    .attr("y", height)
                    .attr("width", legendElementWidth)
                    .attr("height", gridSize / 2)
                    .style("fill", function(d, i) { return colors[i]; });

                legend.append("text")
                    .attr("class", "mono")
                    .text(function(d) { return "≥ " + Math.round(d); })
                    .attr("x", function(d, i) { return legendElementWidth * i; })
                    .attr("y", height + gridSize);

                legend.exit().remove();

            });
    };

    heatmapChart(datasets[0]);

    // var datasetpicker = d3.select("#dataset-picker").selectAll(".dataset-button")
    //     .data(datasets);
    //
    // datasetpicker.enter()
    //     .append("input")
    //     .attr("value", function(d){ return "Dataset " + d })
    //     .attr("type", "button")
    //     .attr("class", "dataset-button")
    //     .on("click", function(d) {
    //         heatmapChart(d);
    //     });

    function textLabelOnClick(d) {
        if(this.id == "en") {
            // window.location.href = "../sequences_sunburst/index.html?type=" + this.id;
        } else {
            console.log("jump to page " + this.id)
            window.location.href = "pie-chart.html?target_lang=" + this.id;
        }
    }

    function chapterLabelOnClick(d) {
        // if(this.id) {
        //     window.location.href = "table.html?chapter=" + this.id;
        // } else {
        //     // console.log("jump to page " + this.id)
        //     // window.location.href = "pie-chart.html?target_lang=" + this.id;
        // }
    }

    function cellOnClick(d) {
        if(d.hour == 2) {
            // Column 2: Basque translation
            window.location.href = "table.html?chapter=" + d.day;
        } else {
            // console.log("jump to page " + this.id)
            // window.location.href = "pie-chart.html?target_lang=" + this.id;
        }
    }

