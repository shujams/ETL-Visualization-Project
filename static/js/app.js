// var svgWidth = 960;
// var svgHeight = 500;

// var margin = {
//   top: 20,
//   right: 40,
//   bottom: 80,
//   left: 100
// };

// var width = svgWidth - margin.left - margin.right;
// var height = svgHeight - margin.top - margin.bottom;

// // Create an SVG wrapper, append an SVG group that will hold our scatter chart,
// // and shift the latter by left and top margins.
// var svg = d3
//   .select("#scatter")
//   .append("svg")
//   .attr("width", svgWidth)
//   .attr("height", svgHeight);

// // Append an SVG group
// var chartGroup = svg.append("g")
//   .attr("transform", `translate(${margin.left}, ${margin.top})`);

function buildCharts(state){
    // Import Data
    d3.json('/api/get_all_data').then(function(data){
        console.log("Read json successful");
        console.log(data);

        // Get data/values under "incidences", "mortalities", "uvs"
        // var incidencesDictionaries = data.incidences;
        // var mortalitiesDictionaries = data.mortalities;
        // var uvsDictionaries = data.uvs;

    });
};

buildCharts();
