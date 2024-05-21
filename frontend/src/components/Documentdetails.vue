<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-2 rounded-top">
                    <h5>Documents</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="Address Proof" class="form-label">Address Proof</label>
                        <input type="file" class="form-control" id="Address Proof" v-on:change="form.addressProof">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="MSMED/Udyam Registration" class="form-label">MSMED/Udyam Registration</label>
                        <input type="file" class="form-control" id="MSMED/Udyam Registration"
                            v-on:change="form.msmedUdyamNumber">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PAN/Aadhar" class="form-label">PAN/Aadhar</label>
                        <input type="file" class="form-control" id="PAN/Aadhar" v-on:change="form.panAadhar">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="ESIC" class="form-label">ESIC</label>
                        <input type="file" class="form-control" id="ESIC" v-on:change="form.esic">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PF" class="form-label">PF</label>
                        <input type="file" class="form-control" id="PF" v-on:change="form.pf">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="TIN/UIN" class="form-label">TIN/UIN</label>
                        <input type="file" class="form-control" id="TIN/UIN" v-on:change="form.tinUin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST</label>
                        <input type="file" class="form-control" id="GST" v-on:change="form.gst">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="CIN" class="form-label">CIN</label>
                        <input type="file" class="form-control" id="CIN" v-on:change="form.cin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="LST/CST" class="form-label">LST/CST</label>
                        <input type="file" class="form-control" id="LST/CST" v-on:change="form.lstCst">
                    </div>
                </div>
                <div class="row">
                <div class="d-flex justify-content-end mt-1 mb-3 col-11">
                <Button type="button" class="savebutton" @click="ValidateEmail()">Save</Button>
            </div>

            <div class="d-flex justify-content-end mt-1 mb-3 col-1 ">
                <Button type="button" class="savebutton" @click="submit()">Submit</Button>
            </div>
        </div>
            </div>
        </div>
    </div>


<!-- Tost Message -->
    <div
      class="toast align-items-center text-white bg-success  border-0"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      :class="{ 'show': showToast }"
    >
      <div class="d-flex">
        <div class="toast-body">
          Details Submitted Sucessfully.
        </div>
        <button
          type="button"
          class="btn-close btn-close-white me-2 m-auto"
          @click="hideToast"
          aria-label="Close"
        ></button>
      </div>
    </div>
</template>

<script>
import { ref, defineComponent, onMounted, reactive } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);

export default defineComponent({
    name: 'ContactDetails',
    setup() {
        const form = reactive({
            addressProof: '',
                msmedUdyamNumber: '',
                panAadhar: '',
                esic: '',
                pf: '',
                tinUin: '',
                gst: '',
                cin: '',
                lstCst: '',
                docname:''
        });
        const loginUser=sessionUser()
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
                        console.log("data", data);
                        form.docname=data.name
                },
                onError: (error) => {
                    console.error('Error:', error);
                    // alert(`An error occurred: ${error.message}`);
                }
            });
        });

        function ValidateEmail() {
            // console.log('values are here', form);
            // const supplier = createResource({
            //     url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
            //     makeParams: () => ({
            //         doc: {
            //             supplier_name: form.supplier_name,
            //             supplier_type: form.supplier_type,
            //             related_party: form.related_party,
            //             supplier_details: form.supplier_details,
            //             docname:form.docname
            //         }
            //     }),
            //     auto: true,
            //     onSuccess: (data) => {
            //         console.log(data)
            //     },
            //     onError: (error) => {
            //         console.error('Error:', error);
            //         alert(`An error occurred: ${error.message}`);
            //     }
            // });
        }
        function submit(){
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.submit_supplier_detail",
                makeParams: () => ({
                    doc: {
                        docname:form.docname,
                        workflow_state:"Approval Pending By Company User Team"
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data)
                    // alert("Details Submitted Sucessfully")
                    showToastMessage()
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
        }
        const showToastMessage = () => {
            showToast.value = true;
            console.log("Details saved successfully");
            setTimeout(() => {
                showToast.value = false;
            }, 1000);
        };

        const hideToast = () => {
            showToast.value = false;
        };
        return {
            form,
            ValidateEmail,
            submit,
            hideToast,
            showToastMessage,
            showToast
        };
    }
});
</script>

<style scoped>
.container {
    height: 80vh;
}

.bg-primary {
    background-color: #2e6bdc !important;
}

.rounded-top {
    border-radius: 10px 10px 0px 0px;
}
.savebutton {
    background-color: #2e6bdc;
    color: white;
    font-size: 1.5rem;
    padding: 1rem;
}
label{
    font-weight:600;
}
h6{
    color: #2e6bdc;
    font-weight: bolder;
}

/* tost css */

.savebutton {
    background-color: #2e6bdc;
    color: white;
    font-size: 1.5rem;
    padding: 0px 20px 0px 20px;
    border-radius: 10px;
}
.toast {
  position: fixed;
  top: 5rem;
  right: 2rem;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}
.toast.show {
  opacity: 1;
}
</style>