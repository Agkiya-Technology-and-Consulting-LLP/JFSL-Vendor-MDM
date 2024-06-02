<!-- <template>
  <p style="color: #2e6bdc;text-align: center;">Code Of Conduct</p>
  <div>
    <div class="pdf-container">
      <iframe :src="pdfUrl" width="100%" height="100%" style="border: none;"></iframe>
    </div>

    <div class="p-1">
      <div class="d-flex justify-content-end pe-3 pe-md-10">
        <button track="click_decline_codeOfConduct"
          class="bg-transparent border-2 border-secondary text-secondary py-2 px-4 rounded"
          @click="logout()">Decline</button>
        <router-link to="/privacyPolicy">
          <button track="click_accept_codeOfConduct" class="bg-secondary text-white py-2 px-4 rounded ms-2"
            @click="accept_code_of_conduct()">Accept the Code of Conduct</button>
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
import { onMounted, ref ,reactive } from 'vue';
import { session ,sessionUser} from '../data/session'
import { createResource } from 'frappe-ui'
const pdfUrl = ref('');
const doc_name=ref('')
const form = reactive({ 
  doc_name:''
})
function logout() {
  session.logout.submit();
}
function accept_code_of_conduct() {
  const supplier = createResource({
    url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.accept_code_of_conduct",
    makeParams: () => ({
      doc:{
        docname:form.doc_name
      }
    }),
    auto: true,
    onSuccess: (data) => {
      console.log(data)
      let url = window.location.origin;
      let targetPath = '/frontend/privacyPolicy'
      let targetUrl = url + targetPath;
      window.location.replace(targetUrl);
    }, onError: (error) => {
      console.log(error)
    }
  })
  const loginUser = sessionUser();
  const supplier_clone = createResource({
      url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",
      makeParams: () => ({
          doc: {
              email: loginUser
          }
      }),
      auto: true,
      onSuccess: (data) => {
        form.doc_name=data.name
        console.log(doc_name.value)
      },
      onError:(error)=>{
        console.log(error)
      }
    })

}


onMounted(() => {
  createResource({
    url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_config",
    makeParams: () => ({}),
    auto: true,
    onSuccess: (data) => {
      console.log(data);
      pdfUrl.value = window.location.origin + data.code_of_conduct_url;
    },
    onError: (error) => {
      console.log(error);
    }
  });
});
// const pdfUrl = "https://uat-jfsl-mdm.frappe.cloud/files/JFSL%20Supplier%20Code%20of%20Conduct.pdf"; 
</script> -->






<template>
  <p style="color: #2e6bdc;text-align: center;">Code Of Conduct</p>
  <div>
    <div class="pdf-container">
      <iframe :src="pdfUrl" width="100%" height="100%" style="border: none;"></iframe>
    </div>

    <div class="p-1">
      <div class="d-flex justify-content-end pe-3 pe-md-10">
        <button track="click_decline_codeOfConduct"
          class="bg-transparent border-2 border-secondary text-secondary py-2 px-4 rounded"
          @click="logout()">Decline</button>
        <button track="click_accept_codeOfConduct" class="bg-secondary text-white py-2 px-4 rounded ms-2"
          @click="accept_code_of_conduct()">Accept the Code of Conduct</button>
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
import { onMounted, ref ,reactive } from 'vue';
import { session ,sessionUser } from '../data/session';
import { createResource } from 'frappe-ui';

const pdfUrl = ref('');
const form = reactive({ 
  doc_name: ''
});

function logout() {
  session.logout.submit();
}

function accept_code_of_conduct() {
  if (!form.doc_name) {
    console.error('doc_name is null or empty');
    return;
  }

  const supplier = createResource({
    url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.accept_code_of_conduct",
    makeParams: () => ({
      doc: {
        docname: form.doc_name
      }
    }),
    auto: true,
    onSuccess: (data) => {
      console.log(data);
      let url = window.location.origin;
      let targetPath = '/frontend/privacyPolicy';
      let targetUrl = url + targetPath;
      window.location.replace(targetUrl);
    }, 
    onError: (error) => {
      console.log(error);
    }
  });
}

function fetchSupplierDetails() {
  const loginUser = sessionUser();
  createResource({
    url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",
    makeParams: () => ({
      doc: {
        email: loginUser
      }
    }),
    auto: true,
    onSuccess: (data) => {
      form.doc_name = data.name;
      console.log(form.doc_name);
    },
    onError: (error) => {
      console.log(error);
    }
  });
}

onMounted(() => {
  createResource({
    url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_config",
    makeParams: () => ({}),
    auto: true,
    onSuccess: (data) => {
      console.log(data);
      pdfUrl.value = window.location.origin + data.code_of_conduct_url;
      fetchSupplierDetails(); // Fetch supplier details after getting config
    },
    onError: (error) => {
      console.log(error);
    }
  });
});
</script>