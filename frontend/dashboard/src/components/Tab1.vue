<script setup>
import { defineProps, computed, reactive } from 'vue';
import BarHorizont from '@/components/BarHorizont.vue';
import BarChart from '@/components/BarChart.vue';
import Card from '@/components/Card.vue';
import List from '@/components/List.vue';

  
const props = defineProps({
  datax: Array,
  datay: Array,
  dataCardProductQuantity: 0,
  dataCardDTQuantity: 0,
  listName: String,
  listData: Array,
  listTableColumns: Object,
});

</script>

<template>
  
  <div class="grid grid-cols-6 gap-3 m-2">

    <div class="col-span-2">

      <div class="grid grid-rows-3 grid-flow-col gap-3">

        <div class="grid grid-cols-2 gap-3">
          <div class="">
            <Card :label="'Количество товара на складе'" :value="dataCardProductQuantity" />
          </div>
          <div class="">
            <Card :label="'Количество ДТ на складе'" :value="dataCardDTQuantity" />
          </div>
        </div>

        <div class=" row-span-2">
          <BarHorizont :name="'bar-h-03'" :title="'ТНВЭД на складе'" :xtitle="'Количество'" :ytitle="'Группа ТНВЭД'"
          :datax="datax"
          :datay="datay" 
          :barcolor="'#00FF7F'" 
          />
        </div>

      </div>

    </div>

    <div class="col-span-4">
      <div class="">
        <List :name="listName" :data="listData" :listTableColumns="listTableColumns" />
      </div>
    </div>

  </div>
  
</template>

<!-- #00E396  #FF69B4  #CD5C5C  #FFA07A  #7B68EE  #00FF7F  #00BFFF -->
