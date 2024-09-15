<script setup>
import { defineProps, ref, reactive, onMounted, computed } from 'vue';
import 'primeicons/primeicons.css';
// import router from '@/router';
import axios from 'axios';
// import { RouterView } from 'vue-router';
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

import Navbar from './components/Navbar.vue';
import Dashboard from './components/Dashboard.vue';
import BarChart from '@/components/BarChart.vue';
import BarHorizont from '@/components/BarHorizont.vue';


const state = reactive({
  data: [],
  isLoading: true,
})

// TABS & WIDGETS
// storageState - cardProductQuantity, cardDtQuantity, barTnvedQuantity, listProductsStorage
// accountBook - cardRecProductQuantity, cardRecDtQuantity, barRecTnvedQuantity, listAccountBook
// reportVehicle - listReportVehicle

async function getData() {
  //
  try {
      state.data = [];

      state.storageState = {};
      state.storageState.barTnvedQuantity = {};
      state.storageState.barTnvedQuantity.datax = [];
      state.storageState.barTnvedQuantity.datay = [];

      state.accountBook = {};
      state.accountBook.barRecTnvedQuantity = {};
      state.accountBook.barRecTnvedQuantity.datax = [];
      state.accountBook.barRecTnvedQuantity.datay = [];

      state.reportVehicle = {};

      const response = await axios.get('http://localhost:8000/dashboard');
      state.data = response.data;

      state.storageState.cardProductQuantity = state.data['product_quantity'][0]['product_quantity'];
      state.storageState.cardDtQuantity = state.data['dt_quantity'][0]['dt_quantity'];
      for (let i of state.data['tnved_quantity']) {
        state.storageState.barTnvedQuantity.datax.push(i['g33']);
        state.storageState.barTnvedQuantity.datay.push(i['cnt'])
      }   
      state.storageState.listProductsStorage = state.data['products_on_storage']

      state.accountBook.cardRecProductQuantity = state.data['received_product_quantity'][0]['received_product_quantity'];
      state.accountBook.cardRecDtQuantity = state.data['received_dt_quantity'][0]['received_dt_quantity'];
      for (let i of state.data['received_tnved_quantity']) {
        state.accountBook.barRecTnvedQuantity.datax.push(i['g33']);
        state.accountBook.barRecTnvedQuantity.datay.push(i['cnt'])
      }   
      state.accountBook.listAccountBook = state.data['account_book']

      state.reportVehicle.listreportVehicle = state.data['report_vehicle']
      


    } catch (error) {
      console.error('Error fetching items', error);
    } finally {
      state.isLoading = false;
    }
};


async function updateData() {
  //
  state.isLoading = true;
  await getData();
};

const handleSubmit = async () => {
  //
  console.log('handle submit!')
}


onMounted(async () => {
    await getData()
});


const storageStateListTableColumns = {
    'gtdnum':'Номер ДТ','name':'Владелец','date_in':'Дата прием','g32':'№ тов.',
    'g31':'Наименование товара','g33_in':'Код ТНВЭД','g31_3':'Кол.доп.ед', 
    'g31_3a':'Ед.изм.', 'g35':'Вес брутто', 'date_chk':'Дата ок.хр.'
}

const accountBookListTableColumns = {
  'gtdnum': 'Номер ДТ', 'name': 'Владелец', 'date_in': 'Дата приема','time_in': 'Время приема',
    'date_chk': 'Дата ок.хр.','g32': '№ тов.','g31': 'Наименование товара','g33_in': 'Код ТНВЭД',
    'g35': 'Вес брутто', 'g31_3': 'Кол.доп.ед', 'g31_3a': 'Ед.изм.', 'doc_num_out': '№ ДТ выдачи',
    'gtdregime_out': 'Режим выдачи', 'date_out': 'Дата выдачи', 'g35_out': 'Выдача брутто',
    'g31_3_out': 'Выд.доп.ед'
}

const reportVehicleListTableColumns = {
  'id':'№ п/п', 'gtdnum':'Номер ДТ', 'g32':'№ тов.', 'g33_in':'Код ТНВЭД', 'g31':'Наименование товара', 'g35':'Вес брутто',
    'g31_3':'Кол.доп.ед', 'g31_3a':'Ед.изм.', 'date_in':'Дата приема', 'place':'Скл.номер', 'date_chk':'Дата ок.хр.', 
       'exp_date':'Срок годности', 'gtdregime_out':'Режим выдачи', 'doc_num_out':'№ ДТ выдачи', 'g33_out':'Код ТНВЭД выдачи',
    'g35_out':'Выдача брутто', 'g31_3_out':'Выд.доп.ед', 'date_out':'Дата выдачи', 
    'g35ost_':'Остаток брутто', 'g31_3ost_':'Остаток Доп.ед',
}


const filterAccountBookDateDocFrom = ref();
const filterAccountBookDateDocTo = ref();

const filterAccountBookDateEnterFrom = ref()
const filterAccountBookDateEnterTo = ref()

const filterReportVehicleDateEnterFrom = ref()
const filterReportVehicleDateExitTo = ref()

const showFiltersBar = ref(false);
const mouseOverFiltersBar = ref(false);

const clearFilters = () => {
  filterAccountBookDateDocFrom.value = '';
  filterAccountBookDateDocTo.value = '';

  filterAccountBookDateEnterFrom.value = ''
  filterAccountBookDateEnterTo.value = ''

  filterReportVehicleDateEnterFrom.value = ''
  filterReportVehicleDateExitTo.value = ''
}

</script>

<template>
<div>
  <nav class="bg-gradient-to-r from-gray-400 to-gray-600 px-10 py-3 text-white overflow-auto">
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
      <div class="header-btn" @click="showFiltersBar=(showFiltersBar) ? false:true">
        <i class="pi pi-filter" style="font-size: 1.3rem"></i></div>
    </div>
  </nav>

  <div v-if="showFiltersBar" class="absolute z-10 right-0 border w-96 h-screen bg-white">
    <div class="p-3 bg-gray-200 overflow-auto">
    <div class="float-left text-xl ">
      Фильтры данных
    </div>
    <div class="float-right cursor-pointer hover:text-gray-500" @click="showFiltersBar=false">
      <i class="pi pi-times" style="font-size: 1.5rem"></i>
    </div>
    </div>

    <form @submit.prevent="handleSubmit" class="mx-0 mt-3 ">

      <div class="mt-5 mb-2 ml-3">КНИГА УЧЁТА</div>

      <div class="mx-5 mb-2">
        <label class="formLabelStyle">date_doc</label>
        <div class="flex border">
          <div>c</div>
          <input
            type="date"
            v-model="filterAccountBookDateDocFrom"
            id="filterAccountBookDateDocFrom"
            name="filterAccountBookDateDocFrom"
            class="formInputStyle"
            placeholder=""
          />
          <div>по</div>
          <input
            type="date"
            v-model="filterAccountBookDateDocTo"
            id="filterAccountBookDateDocTo"
            name="filterAccountBookDateDocTo"
            class="formInputStyle"
            placeholder=""
          />   
        </div>
      </div>

      <div class="mx-5 mb-2">
        <label class="formLabelStyle">Дата приёма</label>
        <div class="flex border">
          <div>c</div>
          <input
            type="date"
            v-model="filterAccountBookDateEnterFrom"
            id="filterAccountBookDateEnterFrom"
            name="filterAccountBookDateEnterFrom"
            class="formInputStyle"
            placeholder=""
          />
          <div>по</div>
          <input
            type="date"
            v-model="filterAccountBookDateEnterTo"
            id="filterAccountBookDateEnterTo"
            name="filterAccountBookDateEnterTo"
            class="formInputStyle"
            placeholder=""
          />   
        </div>
      </div>

      <hr class="mt-7"> 

      <div class="mt-5 mb-2 ml-3">ОТЧЁТ ТС</div>

      <div class="mx-5 mb-2">
        <label class="formLabelStyle">Дата выдачи - Дата приёма</label>
        <div class="flex border">
          <div>c</div>
          <input
            type="date"
            v-model="filterReportVehicleDateEnterFrom"
            id="filterDateDocFrom"
            name="filterDateDocFrom"
            class="formInputStyle"
            placeholder=""
          />
          <div>по</div>
          <input
            type="date"
            v-model="filterReportVehicleDateExitTo"
            id="filterDateDocTo"
            name="filterDateDocTo"
            class="formInputStyle"
            placeholder=""
          />   
        </div>
      </div>


      <div class="mt-10 flex justify-center space-x-5 py-3 px-5 text-center">
        <button
          class="bg-teal-400 text-white font-semibold rounded-full px-3 py-2 w-60
            drop-shadow-md hover:shadow-lg hover:opacity-75"
          type="submit"
        >
        Применить
        </button>
        <button
          class="bg-pink-400 text-white font-semibold rounded-full px-3 py-2 w-60
            drop-shadow-md hover:shadow-lg hover:opacity-75"
          type="button"
          @click="clearFilters()"
        >
        Сбросить
        </button>
      </div>
    </form>

  </div>

  <!-- Show loading spinner while loading is true -->
  <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
    <PulseLoader />
     LOADING DATA...
  </div>

  <!-- Show when loading is done -->
  <div v-else class="bg-gray-50 h-screen">

filterAccountBookDateDocFrom = {{ filterAccountBookDateDocFrom }}<br>
filterAccountBookDateDocTo = {{ filterAccountBookDateDocTo }}<br>
filterAccountBookDateEnterFrom = {{ filterAccountBookDateEnterFrom }}<br>
filterAccountBookDateEnterTo = {{ filterAccountBookDateEnterTo }}<br>
filterReportVehicleDateEnterFrom = {{ filterReportVehicleDateEnterFrom }}<br>
filterReportVehicleDateExitTo = {{ filterReportVehicleDateExitTo }}<br>
  <Dashboard 
    :storageStateBarTnvedQuantityDatax = "state.storageState.barTnvedQuantity.datax" 
    :storageStateBarTnvedQuantityDatay="state.storageState.barTnvedQuantity.datay" 
    :storageStateCardProductQuantity="state.storageState.cardProductQuantity" 
    :storageStateCardDtQuantity="state.storageState.cardDtQuantity" 
    :storageStateListName="'Товары на складе'" 
    :storageStateListProductsStorage="state.storageState.listProductsStorage" 
    :storageStateListTableColumns="storageStateListTableColumns"

    :accountBookBarRecTnvedQuantityDatax = "state.accountBook.barRecTnvedQuantity.datax" 
    :accountBookBarRecTnvedQuantityDatay="state.accountBook.barRecTnvedQuantity.datay" 
    :accountBookCardRecProductQuantity="state.accountBook.cardRecProductQuantity" 
    :accountBookCardRecDtQuantity="state.accountBook.cardRecDtQuantity" 
    :accountBookListName="'Книга учета'" 
    :accountBookListAccountBook="state.accountBook.listAccountBook" 
    :accountBookListTableColumns="accountBookListTableColumns"

    :reportVehicleListName="'Отчет ТС'" 
    :reportVehicleListAccountBook="state.reportVehicle.listreportVehicle" 
    :reportVehicleListTableColumns="reportVehicleListTableColumns"
  /> 

  </div>
</div>
</template>


<style lang="postcss" scoped>
.header-btn {
  @apply mx-3 mt-1 cursor-pointer hover:text-green-400
}

.formLabelStyle {
  @apply mx-1 block text-xs font-bold text-gray-400
}

.formInputStyle {
  @apply border-b-2 text-base font-medium w-36 py-1 px-1 mb-2
  hover:border-indigo-200 focus:outline-none focus:border-indigo-300 cursor-pointer
}
</style>