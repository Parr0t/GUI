var margin = {
        top: 20,
        right: 20,
        bottom: 30,
        left: 50
    },
    width = 660 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;


var parseTime = d3.timeParse("%Y-%m-%d %H:%m:%S.%L"),
    formatTime = d3.timeFormat("%S.%L");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);


var area = d3.area()
    .x(function (d) {
        return x(d.Datetime);
    })
    .y0(height)
    .y1(function (d) {
        return y(d.Values);
    });

// define the line
var valueline = d3.line()
    .x(function (d) {
        return x(d.Datetime);
    })
    .y(function (d) {
        return y(d.Values);
    });



// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("#soundsensor").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

var lineSvg = svg.append("g");

var focus = svg.append("g")
    .style("display", "none");

// Define the div for the tooltip
var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);


// get the data
d3.json("/feinschneiden4_0/soundsensor", function (error, data) {
    if (error) throw error;

    // format the data
    data.forEach(function (d) {
        d.Datetime = parseTime(d.Datetime);
        d.Values = +d.Values;
    });

    // scale the range of the data
    x.domain(d3.extent(data, function (d) {
        return d.Datetime;
    })).range([0,width]);


    y.domain([0, d3.max(data, function (d) {
        return d.Values;
    })]);



    // add the area
    svg.append("path")
        .data([data])
        .attr("class", "area")
        .attr("d", area);

    // add the valueline path.
    svg.append("path")
        .data([data])
        .attr("class", "line")
        .attr("d", valueline);

    // Add the valueline path.
    lineSvg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));


    // Add the scatterplot
    svg.selectAll("dot")
        .data(data)
        .enter().append("circle")
        .style("fill", "darksalmon")
        .attr("r", 3)
        .attr("cx", function(d) { return x(d.Datetime); })
        .attr("cy", function(d) { return y(d.Values); })
        .on("mouseover", function(d) {
        div.transition()
            .duration(200)
            .style("opacity", .9)            ;
        div.html("<span class='tooltipElementsXY'>X:</span> " + formatTime(d.Datetime) + "<hr style='border: none; border-top: 1px solid darkcyan;margin:2px 1px; color: #FFFFFF; background-color: none; height: 1px;'> <span class='tooltipElementsXY'>Y</span>: "  + d.Values)
            .style("left", (d3.event.pageX + 8) + "px")
            .style("top", (d3.event.pageY - 28) + "px");
    }).on("mouseout", function(d) {
        div.transition()
            .duration(300)
            .style("opacity", 0);
    });


    // add the X Axis
    var xAxis = svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // add the Y Axis
    var yAxis = svg.append("g")
        .call(d3.axisLeft(y));







});
