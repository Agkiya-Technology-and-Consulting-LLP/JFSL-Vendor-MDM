<template>
  <p style="color: #2e6bdc;text-align: center;">Code Of Conduct</p>
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
      <router-link to="/privacyPolicy">
        <button track="click_accept_codeOfConduct" class="bg-secondary text-white py-2 px-4 rounded ms-2" @click="accept_code_of_conduct()">Accept the Code of Conduct</button>
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
import {createResource} from 'frappe-ui'

function logout() {
      session.logout.submit();
    }
function accept_code_of_conduct(){
  const supplier = createResource({
                  url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.accept_code_of_conduct",
                  makeParams: () => ({
                  }),
                  auto: true,
                  onSuccess: (data) => {
                    console.log(data)
                    let url = window.location.origin;
                    let targetPath='/frontend/privacyPolicy'
                    let targetUrl = url + targetPath;
                    window.location.replace(targetUrl);
                  },onError :(error)=>{
                    console.log(error)
                  }
                })
  console.log("LLLL")
}
const pdfUrl = "https://uat-jfsl-mdm.frappe.cloud/files/document.pdf"; 
</script>
