<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-2 rounded-top">
                    <h5>Documents</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.addressProof && !form.addressProof }">
                        <label for="AddressProof" class="form-label">Address Proof </label>
                        <input type="file" class="form-control" id="AddressProof"
                            @change="handleFileChange($event, 'address_proof')" @blur="touched.addressProof = false">
                        <div v-if="touched.addressProof && !form.addressProof" class="text-danger">
                            Address Proof is required.
                        </div>
                    </div>

                    <div class="col-md-6 mb-3"
                        :class="{ 'has-error': touched.msmedUdyamNumber && !form.msmedUdyamNumber }">
                        <label for="MSMEDUdyamRegistration" class="form-label">MSMED/Udyam Registration </label>
                        <input type="file" class="form-control" id="MSMEDUdyamRegistration"
                            @change="handleFileChange($event, 'msmedudyam_registration')"
                            @blur="touched.msmedUdyamNumber = false">
                        <div v-if="touched.msmedUdyamNumber && !form.msmedUdyamNumber" class="text-danger">
                            MSMED/Udyam Registration is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.panAadhar && !form.panAadhar }">
                        <label for="PANAadhar" class="form-label">PAN/Aadhar </label>
                        <input type="file" class="form-control" id="PANAadhar"
                            @change="handleFileChange($event, 'panaadhar')" @blur="touched.panAadhar = false">
                        <div v-if="touched.panAadhar && !form.panAadhar" class="text-danger">
                            PAN/Aadhar is required.
                        </div>
                    </div>

                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.esic && !form.esic }">
                        <label for="ESIC" class="form-label">ESIC </label>
                        <input type="file" class="form-control" id="ESIC" @change="handleFileChange($event, 'esic')"
                            @blur="touched.esic = false">
                        <div v-if="touched.esic && !form.esic" class="text-danger">
                            ESIC is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.pf && !form.pf }">
                        <label for="PF" class="form-label">PF </label>
                        <input type="file" class="form-control" id="PF" @change="handleFileChange($event, 'pf')"
                            @blur="touched.pf = false">
                        <div v-if="touched.pf && !form.pf" class="text-danger">
                            PF is required.
                        </div>
                    </div>

                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.tinUin && !form.tinUin }">
                        <label for="TIN_UIN" class="form-label">TIN/UIN </label>
                        <input type="file" class="form-control" id="TIN_UIN"
                            @change="handleFileChange($event, 'tinuin')" @blur="touched.tinUin = false">
                        <div v-if="touched.tinUin && !form.tinUin" class="text-danger">
                            TIN/UIN is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.gst && !form.gst }">
                        <label for="GST" class="form-label">GST </label>
                        <input type="file" class="form-control" id="GST" @change="handleFileChange($event, 'gst')"
                            @blur="touched.gst = false">
                        <div v-if="touched.gst && !form.gst" class="text-danger">
                            GST is required.
                        </div>
                    </div>

                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.cin && !form.cin }">
                        <label for="CIN" class="form-label">CIN </label>
                        <input type="file" class="form-control" id="CIN" @change="handleFileChange($event, 'cin')"
                            @blur="touched.cin = false">
                        <div v-if="touched.cin && !form.cin" class="text-danger">
                            CIN is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.lstCst && !form.lstCst }">
                        <label for="LST_CST" class="form-label">LST/CST </label>
                        <input type="file" class="form-control" id="LST_CST"
                            @change="handleFileChange($event, 'lstCst')" @blur="touched.lstCst = false">
                        <div v-if="touched.lstCst && !form.lstCst" class="text-danger">
                            LST/CST is required.
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="d-flex justify-content-end gap-2 mt-1 mb-3">
                        <!-- <button type="button" class="savebutton" @click="ValidateEmail()"
                            :disabled="!isValid">Save</button> -->
                        <button type="button" class="savebutton" @click="submit()" >Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>



    <!-- Tost Message -->
    <div class="toast align-items-center text-white bg-success  border-0" role="alert" aria-live="assertive"
        aria-atomic="true" :class="{ 'show': showToast }">
        <div class="d-flex">
            <div class="toast-body">
                {{form.sucessMSG}}.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" @click="hideToast"
                aria-label="Close"></button>
        </div>
    </div>

</template>

<script>
import { ref, defineComponent, onMounted, reactive, computed } from "vue";
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
            docname: '',
            sucessMSG:''
        });


        const touched = reactive({
            addressProof: false,
            msmedUdyamNumber: false,
            panAadhar: false,
            esic: false,
            pf: false,
            tinUin: false,
            gst: false,
            cin: false,
            lstCst: false,
        });

        const isValid = computed(() => {
            return form.addressProof
                && form.msmedUdyamNumber
                && form.panAadhar
                && form.esic
                && form.pf
                && form.tinUin
                && form.gst
                && form.cin
                && form.lstCst;
        });

        const loginUser = sessionUser()
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
                    form.docname = data.name
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
                    // alert('File uploaded successfully. File URL:', file_url);
                    showToastMessage("File Upload Sucessfully")
                }
            })
            .catch(error => {
                console.error('Error uploading file:', error);
            });
          
        }
   
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
        function submit() {
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.submit_supplier_detail",
                makeParams: () => ({
                    doc: {
                        docname: form.docname,
                        workflow_state: "Approval Pending By Company User Team"
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data)
                    // alert("Details Submitted Sucessfully")
                    showToastMessage("Details Submitted Sucessfully")
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
        }
        const showToastMessage = (data) => {
            form.sucessMSG=data
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
            touched,
            isValid
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

label {
    font-weight: 600;
}

h6 {
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

:disabled {
    /* background-color: grey; */
    cursor: not-allowed;
}
</style>