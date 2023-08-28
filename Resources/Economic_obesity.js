


d3.json("Income_data_and_obesity.json").then(function(data){ 
    console.log(data)


    var trace1 = {

        x: [1, 2, 3, 4],
      
        y: [10, 15, 13, 17],
      
        mode: 'markers',
      
        type: 'scatter'
      
      };
    Plotly.newPlot('myDiv', data);
});




