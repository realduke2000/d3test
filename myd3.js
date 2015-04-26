function test() {
  alert("called test");
}

function plus() {
  d3.selectAll("path")
  .attr("fill", "red");
  /*for (var i = 0; i < 1000000; i++)
  {
    d3.selectAll("circle")
      .attr("fill","fill:#"+i)
  }
  */
}
