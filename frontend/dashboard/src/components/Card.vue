<script setup>
import VueApexCharts from 'vue3-apexcharts';
import { defineProps, computed, reactive } from 'vue';
  
const props = defineProps({
    label: String,
    value: Number,
});

</script>


<template>
    <div class="m-0 p-2 w-58 h-40 border border-gray-200 rounded-lg drop-shadow-md  
      bg-white text-center hover:drop-shadow-lg flex items-center justify-center">
      <div class="">
        <div class="font-normal">
          {{ label }}
        </div>
        <div class="text-blue-500 pt-3 text-4xl font-normal">
          {{ value }}
        </div>
      </div>
    </div>
</template>

