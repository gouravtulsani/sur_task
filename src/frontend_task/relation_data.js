var relation_data = [['Relation', 'Count']]
fetch('http://localhost:8000/relation_destribution')
.then(response => response.json())
.then(data => {
    for(var i in data.result) {
        var tmp = [data.result[i]['relationship'], data.result[i]['count']]
        relation_data.push(tmp)
    }
})
.catch(error => console.error(error))

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable(relation_data);
    var options = {
        title: 'Relation Destribution'
    };
    var chart = new google.visualization.PieChart(document.getElementById('piechart1'));
    chart.draw(data, options);
}