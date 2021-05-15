<template>
  <div>
    <div id="getuppie"></div>
<!--    <div id="getupbar"></div>-->
  </div>
</template>

<script>
  import echarts from 'echarts';
  import '../../node_modules/echarts/theme/vintage.js';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null
      };
    },
    methods: {
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id), 'vintage');
        this.chart.setOption({
          tooltip: {
            trigger: 'axis'
          },
          toolbox: {
            feature: {
              magicType: {
                type: ['line', 'bar']
              },
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          legend:{
            data: ["销量","售价"]
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              boundrayGap: false,
              data: data.huawei.time
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: '销量/售价',
              data:data.huawei.number
            }

          ],
          series: [
            {
              name: '销量',
              type: 'bar',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              markPoint: {
                data: [
                  {type: 'max', name: '最大值'},
                  {type: 'min', name: '最小值'}
                ]
              },
              data: data.huawei.number
            },
            {
              name: '售价',
              type: 'bar',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              markPoint: {
                data: [
                  {type: 'max', name: '最大值'},
                  {type: 'min', name: '最小值'}
                ]
              },
              data: data.huawei.price
            }

          ]
        });
      },
      drawpie(id, centery) {
        this.chart = echarts.init(document.getElementById(id), 'vintage');
        this.chart.setOption({
          title:{
            text:"2021年Q1国内手机品牌市场份额",
            left:"center",
            top:"25"
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            top: '5%',
            left: 'center'
          },
          series: [
            {
              name: '市场份额',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
              },
              label: {
                show: false,
                position: 'center'
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: '40',
                  fontWeight: 'bold'
                }
              },
              labelLine: {
                show: false
              },
              data: data.marketShare.Q121
            }
          ]
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawpie('getuppie');
        if (document.body.clientWidth < 470) {
          this.drawpie('getuppie', '70%');
        } else {
          this.drawpie('getuppie', '60%');
        }
        // var that = this;
        // var resizeTimer = null;
        // window.onresize = function() {
        //   if (resizeTimer) clearTimeout(resizeTimer);
        //   resizeTimer = setTimeout(function() {
        //     that.drawbar('getupbar');
        //     if (document.body.clientWidth < 470) {
        //       that.drawpie('getuppie', '70%');
        //     } else {
        //       that.drawpie('getuppie', '60%');
        //     }
        //   }, 100);
        // }
      });
    }
  }
</script>

<style scoped>
  #getupbar,
  #getuppie {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    /*box-shadow: 0 0 10px #BF382A;*/
    border-radius: 10px;
  }
  #getuppie {
    margin-top: 30px;
  }
  @media screen and (max-width: 470px) {
    #getuppie {
      height: 500px;
    }
  }
</style>
