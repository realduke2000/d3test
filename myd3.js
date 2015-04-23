function draw() {
    d3.selectAll("p")
      .data(data)
      .enter()
            .text(function (d) {
                return d;
            });
}
