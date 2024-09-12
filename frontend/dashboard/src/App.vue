<script setup>
import { defineProps, ref, reactive, onMounted, computed } from 'vue';
import 'primeicons/primeicons.css';
// import router from '@/router';
import axios from 'axios';
// import { RouterView } from 'vue-router';

import Navbar from './components/Navbar.vue';
import Dashboard from './components/Dashboard.vue';
import BarChart from '@/components/BarChart.vue';
import BarHorizont from '@/components/BarHorizont.vue';


const state = reactive({
  data: [],
  tableFields: [],
  localData: [],
  datay: [],
  datax: [],
})


async function getData() {
  //
  try {
      state.data = [];
      state.tableFields = [];
      state.localData = [];
      state.datay = [];
      state.datax = [];
      state.dataCardProductQuantity = 0;
      state.dataCardDTQuantity = 0;
      state.listData = [];

      const response = await axios.get('http://localhost:8000/dashboard');
      // state.data = response.data;
      state.data = response.data;
      // console.log('data=', state.data)
      // state.tableFields = Object.keys(state.data[0]);

      // for (let xobj of state.data) {
      //   let clonedObj = {...xobj};
      //   state.localData.push(clonedObj);
      // };

      // for (let i of state.localData) {
      //   state.datax.push(i['g33']);
      //   state.datay.push(i['cnt'])
      // }

      // product_quantity
      state.dataCardProductQuantity = state.data['product_quantity'][0]['product_quantity'];

      // dt_quantity
      state.dataCardDTQuantity = state.data['dt_quantity'][0]['dt_quantity'];

      // tnved_quantity
      for (let i of state.data['tnved_quantity']) {
        state.datax.push(i['g33']);
        state.datay.push(i['cnt'])
      }      

      // 
      state.listData = state.data['products_on_storage']

      console.log('listdata =', state.listData)


    } catch (error) {
      console.error('Error fetching books', error);
    }
};


async function updateData() {
  //
  await getData();
};


onMounted(async () => {
    await getData()
});


const listTableColumns = {
    'gtdnum':'Номер ДТ','name':'Владелец','date_in':'Дата прием','g32':'№ тов.',
    'g31':'Наименование товара','g33_in':'Код ТНВЭД','g31_3':'Кол.доп.ед', 
    'g31_3a':'Ед.изм.', 'g35':'Вес брутто', 'date_chk':'Дата ок.хр.'
}

</script>

<template>

  <nav class="bg-gradient-to-r from-green-400 to-blue-500 px-10 py-3 text-white overflow-auto">
    <div class="flex float-left text-xl">
      <div class="px-4 border-r-2">Перспектива</div>
      <div class="px-4 border-r-2">Dashboard</div>
      <div class="px-4">Витрина таможенного склада</div>
    </div>
    <div class="flex float-right">
      <div class="px-4 text-base">09-09-2024 17:30</div>
      <div class="header-btn"><i class="pi pi-refresh" style="font-size: 1.3rem" @click="updateData()"></i></div>
      <div class="header-btn"><i class="pi pi-ellipsis-v" style="font-size: 1.3rem"></i></div>
      <div class="header-btn"><i class="pi pi-sign-out" style="font-size: 1.3rem"></i></div>
      <div class="header-btn"><i class="pi pi-filter" style="font-size: 1.3rem"></i></div>
    </div>
  </nav>

  <div v-if="state.listData" class="bg-gray-50 h-screen">
  <Dashboard :datax="state.datax" :datay="state.datay" 
    :dataCardProductQuantity="state.dataCardProductQuantity" 
    :dataCardDTQuantity="state.dataCardDTQuantity" 
    :listName="'Товары на складе'" :listData="state.listData" 
    :listTableColumns="listTableColumns"
  /> 
  </div>

</template>


<style lang="postcss" scoped>
.header-btn {
  @apply mx-3 mt-1 cursor-pointer hover:text-green-400
}
</style>