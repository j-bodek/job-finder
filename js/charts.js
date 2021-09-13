//  get all charts
let charts = document.querySelectorAll('.myChart');


// specify function to display charts
let displayChart = (chart, data, labels) => {

    let type = chart.dataset.type
    let ctx = chart.getContext('2d')

    if (type == 'bar') {
        let myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Orange', 'Orange', 'Orange', 'Orange'],
                datasets: [{
                    label: '# of Votes',
                    data: [12, 19, 3, 5, 2, 3, 3, 5, 2, 3],
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
                labels: [
                    'Red',
                    'Blue',
                    'Yellow',
                    'Yellow',
                    'Yellow',
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: [300, 50, 100, 200, 120],
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
                labels: ['4000 PLN', '8000 PLN', '3000 PLN', '5000 PLN', '6000 PLN', '7000 PLN', '14000 PLN', '12000 PLN', '10000 PLN', '20000 PLN'],
                datasets: [{
                    label: 'Number of offerts',
                    data: [12, 19, 3, 5, 2, 2, 19, 3, 5, 2],
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
    displayChart(chart, 'data', 'labels')
});