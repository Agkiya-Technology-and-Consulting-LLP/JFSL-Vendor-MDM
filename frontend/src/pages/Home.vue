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
  import { sessionUser } from '../data/session';
  import { createResource } from 'frappe-ui';
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
        const supplier = createResource({
                  url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_supplier_detail",
                  makeParams: () => ({
                      doc: {
                          email: sessionUser()
                      }
                  }),
                  auto: true,
                  onSuccess: (data) => {
                    let url = window.location.origin;
                    let targetPath=''
                      console.log(";;;;;;;",data)
                      if (!data.accept_code_of_conduct){
                        targetPath='/frontend/codeofConduct'
                      }else if (!data.accept_esg_policy){
                        targetPath='/frontend/privacyPolicy'
                      }else{
                        targetPath='/frontend/welcome'
                      }
                      // console.log("::::");
                      // let targetPath = '/frontend/welcome';
                      let targetUrl = url + targetPath;

                      // Check if the current location is already the target URL to prevent infinite loop
                      if (window.location.pathname !== targetPath) {
                        window.location.replace(targetUrl);

                        // Optionally reload the window after a short delay
                        setTimeout(() => {
                          window.location.reload();
                        }, 500); // Adjust the delay as needed
                      }
                  },
                  onError: (error) => {
                      console.error('Error:', error);
                      // alert(`An error occurred: ${error.message}`);
                      let url = window.location.origin;
                      let targetPath='/frontend/codeofConduct'
                      let targetUrl = url + targetPath;
                      if (window.location.pathname !== targetPath) {
                        window.location.replace(targetUrl);

                        // Optionally reload the window after a short delay
                        setTimeout(() => {
                          window.location.reload();
                        }, 500); // Adjust the delay as needed
                      }
                  }
              });
        
      });
  }
  };
  </script>
  <style>
  </style>

