<template>
  <div>
    <AppHeader @toggle-sidebar="toggleSidebar" />
    <main class="flex">
      <Sidebar :is-open="sidebarOpen"/>
      <div class="flex-1 p-4">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script>
import header from '@/components/header.vue'
import Sidebar from '@/components/Sidebar.vue';

export default{
    name:"Home",
    components:{
        AppHeader:header,
        Sidebar
    },
    data() {
    return {
      sidebarOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.sidebarOpen = !this.sidebarOpen;
    }
  }
};
</script>
<style>
</style>

