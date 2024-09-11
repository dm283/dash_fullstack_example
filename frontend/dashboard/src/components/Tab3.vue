<script setup>
import { defineProps, computed, reactive } from 'vue';
import List from '@/components/List.vue';

  
const props = defineProps({
  listName: String,
  listData: Array,
  listTableColumns: Object,
});

</script>

<template>
  
  <div class="border bg-white">

    <List :name="listName" :data="listData" :listTableColumns="listTableColumns" />

  </div>
  
</template>
