//alert("Hello, France!")

init();

w = 700;
h = 700;

//Datasets
dataset = [];
margin = {top: 0, right: 0, bottom: 0, left: 0};

svg = d3.select("body")
          .append("svg")
            .attr("width", w + margin.left + margin.right)
            .attr("height", h + margin.top + margin.bottom);

// Define the div for the tooltip
div = d3.select("body").append("div") 
  .attr("class", "tooltip")       
  .style("opacity", 0);

d3.csv("data/Car.csv")
  .row( (d, i) => {
    return {
      Num_Acc: +d.Num_Acc,
      an: +d.an,
      mois: +d.mois,
      jour: +d.jour,
      hrmn: +d.hrmn,
      lum : +d.lum,
      agg : + d.agg,
      int : +d.int,
      atm : +d.atm,
      col : +d.col,
      com : +d.com,
      adr : d.adr,
      gps : d.gps,
      lat : +d.lat,
      long : +d.long,
      dep : +d.dep
    };
  }
)
  .get( (error, rows) => {
    console.log("Loaded " + rows.length + " rows");
    if (rows.length > 0){
       console.log("First row: ", rows[0])
       console.log("Last row " , rows[rows.length - 1])
    }
    dataset = rows;

    //Scale coordinates
    var x = d3.scaleLinear()
      .domain(d3.extent(rows, (row) => row.long))
      .range([50,600]);
    var y = d3.scaleLinear()
      .domain(d3.extent(rows, (row) => row.lat))
      .range([600,50]);

    //Scale axis
    var xAxis = svg.append("g")
      .attr("transform", "translate(0," + 620 + ")")
      .attr("class", "xaxis")
      .call(d3.axisBottom(x));
    var yAxis = svg.append("g")
      .attr("transform", "translate(0,0)")
      .attr("class", "yaxis")
      .call(d3.axisRight(y));
    //Draw function
})
    //Draw function
draw_tooltip();

function draw_tooltip() {

  svg.selectAll("circle")
      .data(dataset)
      .enter()
      .append("circle")
        .attr("r", 2)
        .attr("cx", (d) => x(d.long))
        .attr("cy", (d) => y(d.lat))
        .attr("class", "circles")
        .attr("opacity", .9)
}

function init() {
  d3.selectAll("svg").remove()

  w = 700;
  h = 700;

  //Datasets
  dataset = [];
  margin = {top: 0, right: 0, bottom: 0, left: 0};

  svg = d3.select("body")
            .append("svg")
              .attr("width", w + margin.left + margin.right)
              .attr("height", h + margin.top + margin.bottom);

  // Define the div for the tooltip
  div = d3.select("body").append("div") 
    .attr("class", "tooltip")       
    .style("opacity", 0);

  scatter = svg.append('g')
        .attr("clip-path", "url(#clip)");

  //For the size of the circle
  rscale = d3.scaleLinear()
    .domain([0,3000000])
    .range([1,30]);

  //Color of the circles (choice)
  colorScale = d3.scaleSequential(d3.interpolateViridis)
    .domain([0, 200]);

}

//This function is called by the buttons on top of the plot
function changeColor(color){
  color = color;
  d3.selectAll("circle")
    .transition()
    .duration(2000)
    .style("fill", color);
}