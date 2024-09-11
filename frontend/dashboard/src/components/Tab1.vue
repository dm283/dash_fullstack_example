<script setup>
import { ref, defineProps, computed, reactive, onMounted } from 'vue';
import BarChart from '@/components/BarChart.vue';
import Card from '@/components/Card.vue';

  
const props = defineProps({
  datax: Array,
  datay: Array,
  dataCardProductQuantity: 0,
  dataCardDTQuantity: 0,
});

</script>

<template>

  <div class="border bg-white text-center">

    <Card :label="'Количество товара на складе'" :value="dataCardProductQuantity" />

    <Card :label="'Количество ДТ на складе'" :value="dataCardDTQuantity" />

    <BarChart :name="'bar-01'" :title="'Принятые ТНВЭД'" :xtitle="'Группа ТНВЭД'" :ytitle="'Количество'"
      :datax="datax" 
      :datay="datay"
      :barcolor="'#00BFFF'" 
    />

  </div>
  
</template>

<!-- #00E396  #FF69B4  #CD5C5C  #FFA07A  #7B68EE  #00FF7F  #00BFFF -->
 