"""
    http://echarts.baidu.com/demo.html#multiple-y-axis
"""
app.title = '影视剧热度与品牌热度关联性'

var colors = ['#5793f3', '#d14a61']

option = {
    color: colors,

    tooltip: {
        trigger: 'axis'
    },
    grid: {
        right: '20%'
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        data: ['剧集平均搜索指数', '品牌平均搜索指数']
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            data: ['好运来临', '好先生', '致青春', '小别离']
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '',
            min: 0,
            max: 500000,
            position: 'left',
            axisLine: {
                lineStyle: {
                    color: colors[0]
                }
            },
            axisLabel: {
                formatter: '{value}'
            }
        },
        {
            type: '',
            name: '',
            min: 0,
            max: 6000,
            position: 'right',
            offset: 0,
            axisLine: {
            },
        },
        {
            type: 'value',
            name: '',
            min: 0,
            max: 6000,
            position: 'right',
            axisLine: {
                lineStyle: {
                    color: colors[1]
                }
            },
            axisLabel: {
                formatter: '{value}'
            }
        },
    ],
    series: [
        {
            name: '剧集平均搜索指数',
            type: 'bar',
            data: [10823, 459195, 133238, 200020]
        },
        {
            name: '品牌平均搜索指数',
            type: 'line',
            yAxisIndex: 2,
            data: [1056, 4973, 3039, 3143]
        },
    ]
}
