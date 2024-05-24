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
                        <input type="file" class="form-control" id="Address Proof" @change="handleFileChange($event,'address_proof')" v-on:change="form.addressProof">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="MSMED/Udyam Registration" class="form-label">MSMED/Udyam Registration</label>
                        <input type="file" class="form-control" id="MSMED/Udyam Registration"
                            v-on:change="form.msmedUdyamNumber" @change="handleFileChange($event,'msmedudyam_registration')">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PAN/Aadhar" class="form-label">PAN/Aadhar</label>
                        <input type="file" class="form-control" id="PAN/Aadhar" @change="handleFileChange($event,'panaadhar')" v-on:change="form.panAadhar">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="ESIC" class="form-label">ESIC</label>
                        <input type="file" class="form-control" id="ESIC" @change="handleFileChange($event,'esic')" v-on:change="form.esic">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PF" class="form-label">PF</label>
                        <input type="file" class="form-control" id="PF" @change="handleFileChange($event,'pf')" v-on:change="form.pf">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="TIN/UIN" class="form-label">TIN/UIN</label>
                        <input type="file" class="form-control" id="TIN/UIN" @change="handleFileChange($event,'tinuin')" v-on:change="form.tinUin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST</label>
                        <input type="file" class="form-control" id="GST" @change="handleFileChange($event,'gst')" v-on:change="form.gst">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="CIN" class="form-label">CIN</label>
                        <input type="file" class="form-control" id="CIN" @change="handleFileChange($event,'cin_attach')" v-on:change="form.cin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="LST/CST" class="form-label">LST/CST</label>
                        <input type="file" class="form-control" id="LST/CST" @change="handleFileChange($event,'lstcst')" v-on:change="form.lstCst">
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
        const handleFileChange=(event,field)=> {
            const file = event.target.files[0];
            var formData = new FormData();
            formData.append('file', file);
            formData.append('doctype',"Supplier Clone");
            formData.append('docname', form.docname);
            formData.append('is_private', 0);  // Change to 1 if the file should be private
            formData.append('fieldname',field)
            formData.append('folder',"Home")
            formData.append('attached_to_field',field)
            fetch('/api/method/upload_file', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.message) {
                    var file_url = data.message.file_url;
                    alert('File uploaded successfully. File URL:', file_url);
                }
            })
            .catch(error => {
                console.error('Error uploading file:', error);
            });
          
            // reader.readAsBinaryString(file);
        }
        // const handleMSMEFileChange=(event,field)=>{
        //     const file = event.target.files[0];
        //     var formData = new FormData();
        //     formData.append('file', file);
        //     formData.append('doctype',"Supplier Clone");
        //     formData.append('docname', form.docname);
        //     formData.append('is_private', 0);  // Change to 1 if the file should be private
        //     formData.append('fieldname',"msmedudyam_registration")
        //     formData.append('folder',"Home")
        //     formData.append('attached_to_field',"msmedudyam_registration")
        //     fetch('/api/method/upload_file', {
        //         method: 'POST',
        //         body: formData
        //     })
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data);
        //         if (data.message) {
        //             var file_url = data.message.file_url;
        //             alert('File uploaded successfully. File URL:', file_url);
        //         }
        //     })
        //     .catch(error => {
        //         console.error('Error uploading file:', error);
        //     });
          
        //     // reader.readAsBinaryString(file);
        // }
        // const handlePAN_AadharFileChange = (event,field)=>{
        //     const file = event.target.files[0];
        //     var formData = new FormData();
        //     formData.append('file', file);
        //     formData.append('doctype',"Supplier Clone");
        //     formData.append('docname', form.docname);
        //     formData.append('is_private', 0);  // Change to 1 if the file should be private
        //     formData.append('fieldname',field)
        //     formData.append('folder',"Home")
        //     formData.append('attached_to_field',field)
        //     fetch('/api/method/upload_file', {
        //         method: 'POST',
        //         body: formData
        //     })
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data);
        //         if (data.message) {
        //             var file_url = data.message.file_url;
        //             alert('File uploaded successfully. File URL:', file_url);
        //         }
        //     })
        //     .catch(error => {
        //         console.error('Error uploading file:', error);
        //     })
        // }
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
            showToast,
            handleFileChange,
            // handleMSMEFileChange,
            // handlePAN_AadharFileChange
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