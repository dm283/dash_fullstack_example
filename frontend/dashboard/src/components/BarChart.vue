<script setup>
import VueApexCharts from 'vue3-apexcharts';
import { defineProps, computed, reactive } from 'vue';
  
const props = defineProps({
    name: String,
    title: String,
    xtitle: String,
    ytitle: String,
    barcolor: String,
    datax: Array,
    datay: Array,
});

console.log('check barchart data =', props.datax)

// const name = props.name;
const apexcharts = VueApexCharts;

const options = {
  chart: {
    id: 'basic-bar'
  },
  title: {
    text: props.title,
    style: {fontSize: '20px', fontWeight: 'bold', color: 'DarkSlategray', }
  },
  colors: [props.barcolor],
  xaxis: {
    title: { text: props.xtitle, style: {fontSize: '14px', fontWeight: 'bold', color: 'DarkSlategray', }},
    categories: props.datax,
  },
  yaxis: {
    title: { text: props.ytitle, style: {fontSize: '14px', fontWeight: 'bold', color: 'DarkSlategray', }},
  },
  dataLabels: {
    style: {
      fontSize: '13px',
      color: 'white',
    }
  },
  // fill: {
  //   type: 'gradient',
  //   gradient: {
  //     shade: 'dark',
  //     type: "horizontal",
  //     shadeIntensity: 0.5,
  //     gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
  //     inverseColors: true,
  //     opacityFrom: 1,
  //     opacityTo: 1,
  //     stops: [0, 50, 100],
  //     colorStops: []
  //   }
  // }
};


const computedSeries = computed(() => {
  //
  let series = [{
    name: 'количество',
    data: props.datay,
  }];
  return series;
});

</script>


<template>
  <div class="inline-block drop-shadow-md border border-gray-200 bg-white
    rounded-md m-5 p-3 hover:drop-shadow-lg">  
    <apexcharts width="400" height="280" type="bar" :options="options" :series="computedSeries"
    ></apexcharts>  
  </div>
</template>

<!-- width="500" height="350" -->
 <!-- 400 - 280 -->

