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
                labels: [3000, 3670, 4340, 5010, 5680, 6350, 7020, 7690, 8360, 9030, 9700, 10370, 11040, 11710, 12380, 13050, 13720, 14390, 15060, 15730, 16400, 17070, 17740, 18410, 19080, 19750, 20420, 21090, 21760, 22430, 23100, 23770, 24440, 25110, 25780, 26450, 27120, 27790, 28460, 29130, 29800, 30470, 31140, 31810, 32480, 33150, 33820, 34490, 35160, 35830, 36500, 37170, 37840, 38510, 39180, 39850, 40520, 41190, 41860, 42530, 43200, 43870, 44540, 45210, 45880, 46550, 47220, 47890, 48560, 49230, 49900, 50570, 51240, 51910, 52580, 53250, 53920, 54590, 55260, 55930, 56600, 57270, 57940, 58610, 59280, 59950, 60620, 61290, 61960, 62630, 63300, 63970, 64640, 65310, 65980, 66650, 67320, 67990, 68660, 69330],
                datasets: [{
                    label: 'Number of offerts',
                    data: [1.0, 1.0, 1.0, 2.0, 2.0, 7.0, 13.0, 13.0, 14.0, 15.0, 15.0, 16.0, 15.0, 15.0, 16.0, 18.0, 19.0, 18.0, 16.0, 17.0, 18.0, 19.0, 20.0, 20.0, 20.0, 21.0, 22.0, 18.0, 17.0, 15.0, 13.0, 12.0, 11.0, 8.0, 8.0, 6.0, 6.0, 6.0, 6.0, 4.0, 4.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
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