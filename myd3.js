function test() {
  alert("called test");
}

function plus() {

}

function circle() {
  circleRadii = [40,20,10];
  var svgContainer = d3.select("body")
                      .append("svg")
                      .attr("width", 600)
                      .attr("height", 100);

  var circles = svgContainer.selectAll("circle")
                            .data(circleRadii)
                            .enter()
                            .append("circle");

  var circleAttributes = circles
                                .attr("cx", 50)
                                .attr("cy", 50)
                                .attr("r", function(d) { return d;})
                                .style("fill", function(d) {
                                  if (d == 40) { return "green"; }
                                  if (d == 20) {return "purple";}
                                  if (d == 10) {return "red";}
                                });

}

function jsonCircle() {
  var jsonCircles = [
    {
     "x_axis": 30,
     "y_axis": 30,
     "radius": 20,
     "color" : "green"
    }, {
     "x_axis": 70,
     "y_axis": 70,
     "radius": 20,
     "color" : "purple"
    }, {
     "x_axis": 110,
     "y_axis": 100,
     "radius": 20,
     "color" : "red"
  }];
  var svgContainer = d3.select("body")
                      .append("svg")
                      .attr("width", 200)
                      .attr("height", 200);
  var circles = svgContainer.selectAll("circle")
                            .data(jsonCircles)
                            .enter()
                            .append("circle");
  circles.attr("cx", function(d) {return d.x_axis;})
          .attr("cy", function(d) {return d.y_axis;})
          .attr("r", function(d) {return d.radius;})
          .style("fill", function(d) {return d.color;});
}
