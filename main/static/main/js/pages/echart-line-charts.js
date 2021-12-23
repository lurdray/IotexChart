if( $('#e_chart_2').length > 0 ){
		


		eChart_1.setOption(option);
		eChart_1.resize();
	}$(function() {
    "use strict";
    // ------------------------------
        
            
        
        
    // ------------------------------
    // Basic line chart
    // ------------------------------
    // based on prepared DOM, initialize echarts instance
        var gradiantChart = echarts.init(document.getElementById('g-line'));

        // specify chart configuration item and data
        var data = [

        {% for item in data %}
            ["{{ item.pub_date.isoformat.0 }}{{ item.pub_date.isoformat.1 }}{{ item.pub_date.isoformat.2 }}{{ item.pub_date.isoformat.3 }}{{ item.pub_date.isoformat.4 }}{{ item.pub_date.isoformat.5 }}{{ item.pub_date.isoformat.6 }}{{ item.pub_date.isoformat.7 }}{{ item.pub_date.isoformat.8 }}{{ item.pub_date.isoformat.9 }}",{{ item.price }}],
        {% endfor %}

        var dateList = data.map(function (item) {
            return item[0];
        });
        var valueList = data.map(function (item) {
            return item[1];
        });

        var option = {

            // Make gradient line here
            visualMap: [{
                show: false,
                type: 'continuous',
                seriesIndex: 0,
                min: 0,
                max: 400
            }, {
                show: false,
                type: 'continuous',
                seriesIndex: 1,
                dimension: 0,
                min: 0,
                max: dateList.length - 1
            }],

            
            title: [{
                left: 'center',
                text: 'Gradient along the y axis'
            }],
            tooltip: {
                trigger: 'axis'
            },
            
            xAxis: [{
                data: dateList
            }, {
                data: dateList,
                gridIndex: 1
            }],
            yAxis: [{
                splitLine: {show: false}
            }, {
                splitLine: {show: false},
                gridIndex: 1
            }],
            grid: [{
                bottom: '60%',
                left:'3%',
                right:'3%'
            }, {
                top: '60%',
                left:'3%',
                right:'3%'
            }],
            
            series: [{
                type: 'line',
                showSymbol: false,
                data: valueList
            }, {
                type: 'line',
                showSymbol: false,
                data: valueList,
                xAxisIndex: 1,
                yAxisIndex: 1
            }]
        };
        // use configuration item and data specified to show chart
        gradiantChart.setOption(option);
    
    
       //------------------------------------------------------
       // Resize chart on menu width change and window resize
       //------------------------------------------------------
        $(function () {

                // Resize chart on menu width change and window resize
                $(window).on('resize', resize);
                $(".sidebartoggler").on('click', resize);

                // Resize function
                function resize() {
                    setTimeout(function() {

                        // Resize chart
                        myChart.resize();
                        bareaChart.resize();
                        stackedChart.resize();
                        stackedareaChart.resize();
                        gradiantChart.resize();
                    }, 200);
                }
            });
		
		
    
		
		
		
});