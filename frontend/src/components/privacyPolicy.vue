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
          <button track="click_accept_codeOfConduct" class="bg-secondary text-white py-2 px-4 rounded ms-2" @click="save()">Accept policy</button>
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
  import { ref ,onMounted} from 'vue';
  import { session, sessionUser } from '../data/session'
  import {createResource} from 'frappe-ui'
  const docname=ref('')
  function logout() {
        session.logout.submit();
      }
      let loginUser= sessionUser()
      onMounted(() => {
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",
                makeParams: () => ({
                    doc: {
                        email: loginUser
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    // if (data && data.supplier_name !== undefined) {
                    //     console.log(data);
                    //     docname=data.name
                    //     console.log("<><><><><><><><><><><<<><<",docname)
                    // } else {
                        docname.value=data.name
                        console.log("Received data is not in expected format", docname.value);
                        
                    // }
                },
                onError: (error) => {
                    console.error('Error:', error);
                    // alert(`An error occurred: ${error.message}`);
                }
            });
        });
  function save(){
    console.log("................",docname)
    const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        accept_esg_policy:1,
                        docname:docname.value
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data)
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
  }
  const pdfUrl = "https://uat-jfsl-mdm.frappe.cloud/files/JFSL%20Supplier%20Code%20of%20Conduct.pdf"; 
  </script>
  