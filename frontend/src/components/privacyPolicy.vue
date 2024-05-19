<template>
    <p style="color: #2e6bdc;text-align: center;">ESG Policy</p>
    <div>
      <div class="pdf-container">
        <iframe
          :src="pdfUrl"
          width="100%"
          height="100%"
          style="border: none;"
        ></iframe>
      </div>
  
      <div class="p-1">
        <div class="d-flex justify-content-end pe-3 pe-md-10">
          <button track="click_decline_codeOfConduct" class="bg-transparent border-2 border-secondary text-secondary py-2 px-4 rounded" @click="logout()">Decline</button>
        <router-link to="/welcome">
          <button track="click_accept_codeOfConduct" class="bg-secondary text-white py-2 px-4 rounded ms-2">Accept policy</button>
        </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .pdf-container {
    height: 70vh; 
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>
  
  <script setup>
  import { ref } from 'vue';
  import { session } from '../data/session'
  
  function logout() {
        session.logout.submit();
      }
  
  const pdfUrl = "http://127.0.0.1:8001/files/document.pdf"; 
  </script>
  