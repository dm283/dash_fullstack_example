<script setup>
import { ref, defineProps, computed, reactive } from 'vue';
import Tab1 from '@/components/Tab1.vue';
import Tab2 from '@/components/Tab2.vue';
import Tab3 from '@/components/Tab3.vue';

  
const props = defineProps({
  datax: Array,
  datay: Array,
  dataCardProductQuantity: 0,
  dataCardDTQuantity: 0,
  listName: String,
  listData: Array,
  listTableColumns: Object,
});

const openTab = ref(1);

const toggleTabs = (tabNumber) => {
  openTab.value = tabNumber;
};

</script>

<template>
  
  <nav class="border flex bg-blue-50 text-indigo-500">
    <div :class="{'navTabsSelected': openTab == 1, 'navTabs': openTab != 1}" @click="toggleTabs(1)">Состояние склада</div>
    <div :class="{'navTabsSelected': openTab == 2, 'navTabs': openTab != 2}" @click="toggleTabs(2)">Книга учета</div>
    <div :class="{'navTabsSelected': openTab == 3, 'navTabs': openTab != 3}" @click="toggleTabs(3)">Отчет ТС</div>
  </nav>

  <div id="dashboardContent" class="">
    <div v-if="openTab == 1">
      <Tab1 :datax="datax" :datay="datay" 
        :dataCardProductQuantity="dataCardProductQuantity" 
        :dataCardDTQuantity="dataCardDTQuantity"
        :listName="listName" :listData="listData" :listTableColumns="listTableColumns"
      />
    </div>
    <div v-if="openTab == 2">
      <Tab2 
      />
    </div>
    <div v-if="openTab == 3">
      <Tab3 :listName="listName" :listData="listData" :listTableColumns="listTableColumns" />
    </div>
  </div>
  
</template>


<style lang="postcss" scoped>
.navTabs {
  @apply border rounded-t-lg px-5 py-2 cursor-pointer hover:text-indigo-600
}

.navTabsSelected {
    @apply bg-white border rounded-t-lg px-5 py-2 cursor-pointer hover:text-indigo-600
  }
</style>