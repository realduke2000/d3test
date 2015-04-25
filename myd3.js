function test() {
  alert("called test");
}

function plus() {

var i = 1;
  d3.selectAll("circle")
  .attr("fill", "fill:#" + i);
  /*for (var i = 0; i < 1000000; i++)
  {
    d3.selectAll("circle")
      .attr("fill","fill:#"+i)
  }
  */
}
