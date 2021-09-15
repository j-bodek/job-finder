//  get all charts
let charts = document.querySelectorAll('.myChart');

// specify function to display charts
let displayChart = (chart, received_data) => {

    let type = chart.dataset.type
    let datas = chart.dataset.data
    let ctx = chart.getContext('2d')


    if (type == 'bar') {
        let myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: received_data[datas].labels,
                datasets: [{
                    label: 'Number of offers',
                    data: received_data[datas].data,
                    backgroundColor: [
                        'rgba(249, 65, 68, 0.7)',
                        'rgba(243, 114, 44, 0.7)',
                        'rgba(248, 150, 30, 0.7)',
                        'rgba(249, 132, 74, 0.7)',
                        'rgba(249, 199, 79, 0.7)',
                        'rgba(144, 190, 109, 0.7)',
                        'rgba(67, 170, 139, 0.7)',
                        'rgba(77, 144, 142, 0.7)',
                        'rgba(87, 117, 144, 0.7)',
                        'rgba(39, 125, 161, 0.7)',
                    ],
                    borderColor: [
                        'rgba(249, 65, 68, 1)',
                        'rgba(243, 114, 44, 1)',
                        'rgba(248, 150, 30, 1)',
                        'rgba(249, 132, 74, 1)',
                        'rgba(249, 199, 79, 1)',
                        'rgba(144, 190, 109, 1)',
                        'rgba(67, 170, 139, 1)',
                        'rgba(77, 144, 142, 1)',
                        'rgba(87, 117, 144, 1)',
                        'rgba(39, 125, 161, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });


    }
    if (type == 'pie') {
        let myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: received_data[datas].labels,
                datasets: [{
                    label: 'Number of offers',
                    data: received_data[datas].data,
                    backgroundColor: [
                        'rgb(249, 65, 68, 0.7)',
                        'rgb(249, 132, 74, 0.7)',
                        'rgb(249, 199, 79, 0.7)',
                        'rgb(144, 190, 109, 0.7)',
                        'rgb(39, 125, 161, 0.7)',
                    ],
                    hoverOffset: 4
                }]

            },
        });


    }
    if (type == 'line') {

        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: received_data[datas].labels,
                datasets: [{
                    label: 'Number of offers',
                    data: received_data[datas].data,
                    backgroundColor: 'rgba(249, 65, 68, 0.7)',
                    borderColor: 'rgba(249, 65, 68, 1)',
                    borderWidth: 5,
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        myChart.data.datasets.forEach(dataset => {
            dataset.fill = 'start';
        });
        myChart.options.elements.line.tension = true ? 0.4 : 0;
        myChart.update();
    }

}





// display charts
charts.forEach(chart => {
    displayChart(chart, received_data)
});