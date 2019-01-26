var sex_data = [['Sex', 'Count']]
fetch('http://localhost:8000/sex_destribution')
.then(response => response.json())
.then(data => {
    for(var i in data.result) {
        var tmp = [data.result[i]['sex'], data.result[i]['count']]
        sex_data.push(tmp)
    }
})
.catch(error => console.error(error))

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable(sex_data);
    var options = {
        title: 'Sex Destribution'
    };
    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}