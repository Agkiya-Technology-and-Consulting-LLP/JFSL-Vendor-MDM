<template>
      <header class="headers text-white flex justify-between items-center h-16">
    <div>
      <button @click="toggleSidebar" class="text-xl" style="background-color:#2352a9; padding: 1.25rem;">
        <span ><i class="fa fa-solid fa-bars h-5.5 w-6" ></i></span>
      </button>
      <span class="hidden md:inline-block text-3xl ml-4 !mt-0"><strong>JFSL </strong>Supplier Portal</span>
    </div>
    <nav class="md:flex items-center space-x-6 mr-12">
      <a href="http://127.0.0.1:8001/files/Supplier%20Onboarding%20guideline.pdf" class="hover:text-gray-300 text-white no-underline"><i class="fa-solid fa-circle-info h-6"></i></a>
      <a href="#" class="hover:text-gray-300 text-white no-underline"><i class="fa-solid fa-user h-6"></i></a>
      <a href="#" class="hover:text-gray-300 text-white no-underline" @click="logout()"><i class="fa-solid fa-right-from-bracket h-6"></i></a>
    </nav>
  </header>
</template>

<script>
import { session } from '../data/session'

export default {
  methods: {
    toggleSidebar() {
      this.$emit('toggle-sidebar');
    },

    logout() {
      session.logout.submit();
    }
  }
};
</script>

<style>
.headers{
background-color:#2e6bdc;
}
</style>

