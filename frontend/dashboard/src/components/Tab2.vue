<script setup>
import { defineProps, computed, reactive } from 'vue';
import BarHorizont from '@/components/BarHorizont.vue';
import BarChart from '@/components/BarChart.vue';

  
const props = defineProps({
  datax: Array,
  datay: Array,
});

</script>

<template>
  
  <div class="border bg-white text-center">

    <BarHorizont :name="'bar-h-03'" :title="'ТНВЭД на складе'" :xtitle="'Количество'" :ytitle="'Группа ТНВЭД'"
      :datax="datax"
      :datay="datay" 
      :barcolor="'#FF69B4'" 
    />
    <BarChart :name="'bar-01'" :title="'Принятые ТНВЭД'" :xtitle="'Группа ТНВЭД'" :ytitle="'Количество'"
      :datax="datax" 
      :datay="datay"
      :barcolor="'#00BFFF'" 
    />

  </div>
  
</template>
