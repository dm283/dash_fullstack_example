<script setup>
import VueApexCharts from 'vue3-apexcharts';
import { defineProps, computed, reactive } from 'vue';
  
const props = defineProps({
    label: String,
    value: Number,
});

</script>


<template>
    <div class="w-64 h-30 drop-shadow-md border border-gray-200 bg-white rounded-md m-5 p-3 hover:drop-shadow-lg">
      <div class="">
        {{ label }}
      </div>
      <div class="text-blue-500 pt-3 text-4xl font-normal">
        {{ value }}
      </div>
    </div>
</template>

