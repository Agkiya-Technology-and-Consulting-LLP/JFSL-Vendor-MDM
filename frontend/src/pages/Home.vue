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
import { ref, defineComponent, onMounted, watch } from "vue";

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
  },
  setup() {
    onMounted(() => {
      console.log("::::");
      let url = window.location.origin;
      let targetPath = '/frontend/welcome';
      let targetUrl = url + targetPath;

      // Check if the current location is already the target URL to prevent infinite loop
      if (window.location.pathname !== targetPath) {
        window.location.replace(targetUrl);

        // Optionally reload the window after a short delay
        setTimeout(() => {
          window.location.reload();
        }, 500); // Adjust the delay as needed
      }
    });
}
};
</script>
<style>
</style>

