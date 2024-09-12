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

  Книга учета
  
</template>

<!-- #00E396  #FF69B4  #CD5C5C  #FFA07A  #7B68EE  #00FF7F  #00BFFF -->
 