<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-2 rounded-top">
                    <h5>Documents</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.addressProof && !form.addressProof }">
                        <label for="AddressProof" class="form-label">Aadhar card <span class="text-danger">*</span></label>
                        <input type="file" class="form-control" id="AddressProof"
                            @change="handleFileChange($event, 'address_proof')" @blur="touched.addressProof = true" :disabled="isReadonly">
                        <!-- <div v-if="touched.addressProof && !form.addressProof" class="text-danger">
                            Aadhar is required.
                        </div> -->
                    </div>
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.cheque && !form.cheque }">
                        <label for="cheque" class="form-label">Cancelled cheque <span class="text-danger">*</span> </label>
                        <input type="file" class="form-control" id="cheque"
                            @change="handleFileChange($event, 'cheque')" @blur="touched.cheque = true" :disabled="isReadonly">
                        <!-- <div v-if="touched.cheque && !form.cheque" class="text-danger">
                            cancelled cheque required.
                        </div> -->
                    </div>

                   
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.panAadhar && !form.panAadhar }">
                        <label for="PANAadhar" class="form-label">PAN Card <span class="text-danger">*</span> </label>
                        <input type="file" class="form-control" id="PANAadhar"
                            @change="handleFileChange($event, 'panaadhar')" @blur="touched.panAadhar = true" :disabled="isReadonly">
                        <!-- <div v-if="touched.panAadhar && !form.panAadhar" class="text-danger">
                            PAN is required.
                        </div> -->
                    </div>

                    <div class="col-md-6 mb-3"
                        :class="{ 'has-error': touched.msmedUdyamNumber && !form.msmedUdyamNumber }">
                        <label for="MSMEDUdyamRegistration" class="form-label">MSMED/Udyam Registration </label>
                        <input type="file" class="form-control" id="MSMEDUdyamRegistration"
                            @change="handleFileChange($event, 'msmedudyam_registration')"
                            @blur="touched.msmedUdyamNumber = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.msmedUdyamNumber && !form.msmedUdyamNumber" class="text-danger">
                            MSMED/Udyam Registration is required.
                        </div> -->
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.pf && !form.pf }">
                        <label for="PF" class="form-label">PF </label>
                        <input type="file" class="form-control" id="PF" @change="handleFileChange($event, 'pf')"
                            @blur="touched.pf = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.pf && !form.pf" class="text-danger">
                            PF is required.
                        </div> -->
                    </div>

                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.tinUin && !form.tinUin }">
                        <label for="TIN_UIN" class="form-label">TIN/UIN </label>
                        <input type="file" class="form-control" id="TIN_UIN"
                            @change="handleFileChange($event, 'tinuin')" @blur="touched.tinUin = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.tinUin && !form.tinUin" class="text-danger">
                            TIN/UIN is required.
                        </div> -->
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.gst && !form.gst }">
                        <label for="GST" class="form-label">GST </label>
                        <input type="file" class="form-control" id="GST" @change="handleFileChange($event, 'gst')"
                            @blur="touched.gst = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.gst && !form.gst" class="text-danger">
                            GST is required.
                        </div> -->
                    </div>

                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.cin && !form.cin }">
                        <label for="CIN" class="form-label">CIN </label>
                        <input type="file" class="form-control" id="CIN" @change="handleFileChange($event, 'cin')"
                            @blur="touched.cin = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.cin && !form.cin" class="text-danger">
                            CIN is required.
                        </div> -->
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.lstCst && !form.lstCst }">
                        <label for="LST_CST" class="form-label">LST/CST </label>
                        <input type="file" class="form-control" id="LST_CST"
                            @change="handleFileChange($event, 'lstCst')" @blur="touched.lstCst = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.lstCst && !form.lstCst" class="text-danger">
                            LST/CST is required.
                        </div> -->
                    </div>
                    <div class="col-md-6 mb-3" :class="{ 'has-error': touched.esic && !form.esic }">
                        <label for="ESIC" class="form-label">ESIC </label>
                        <input type="file" class="form-control" id="ESIC" @change="handleFileChange($event, 'esic')"
                            @blur="touched.esic = false" :disabled="isReadonly">
                        <!-- <div v-if="touched.esic && !form.esic" class="text-danger">
                            ESIC is required.
                        </div> -->
                    </div>

                    
                </div>

                <div class="row" v-if="!isReadonly && isupdate">
                    <div class="d-flex justify-content-end gap-2 mt-1 mb-3">
                        <router-link to="/accountdetails" class="btn btn-primary"><button>Back</button></router-link>
                        <button type="button" class="btn btn-primary" @click="submit()" :disabled="isReadonly" v-if="!isReadonly">Submit</button>
                    </div>
                </div>
                <!-- <div class="row" v-if="!isupdate"> -->
                <div class="row" v-if="!isupdate">

                    <div class="d-flex justify-content-end gap-2 mt-1 mb-3">
                        <button type="button" class="btn btn-primary" @click="update()" v-if="!isReadonly">Update</button>
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

    <!-- Tost Error Message -->
    <div class="toast align-items-center text-white bg-danger  border-0" role="alert" aria-live="assertive" aria-atomic="true" :class="{ 'show': showErrorToast }" >
        <div class="d-flex">
            <div class="toast-body">
                {{form.error}}.
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" @click="hideErrorToast" aria-label="Close"></button>
        </div>
    </div>

</template>

<script>
import { ref, defineComponent, onMounted, reactive, computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);
const showErrorToast = ref(false)
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
            cheque: '',
            docname: '',
            sucessMSG:'',
            validateSubmit:false
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
            cheque: false,
            // validateSubmit: false,
        });

        const isValid = computed(() => {
            return form.addressProof
                // && form.msmedUdyamNumber
                && form.panAadhar
                // && form.esic
                // && form.pf
                // && form.tinUin
                // && form.gst
                // && form.cin
                // && form.lstCst
                && form.cheque;
        });

        const loginUser = sessionUser()
        const workflowState = ref('');
        // const isReadonly = computed(() => workflowState.value !== 'Saved');
        const isReadonly = computed(() => {
            return !['Saved', 'Change Requested', 'Approved'].includes(workflowState.value);
        });
        const isupdate = computed(()=>{
            return !['Change Requested', 'Approved'].includes(workflowState.value)
        })

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
                    console.log("data coming from documents", data);
                    form.docname = data.name
                    // console.log(data.email_id)
                    const fields =['company_name','permanent_account_number','name_','addressline_1','country','city','region','pincode','residential_status','salutation','first_name','email_id','contact_number','account_number','confirm_account_number','ifsc_code','address_proof','panaadhar','cheque']
                    fields.forEach((field)=>{
                        // console.log(field)
                        if (!data[field]) {
                            console.log(`Missing field: ${field}`);
                            form.validateSubmit=true
                        }   
                    })
                    console.log("validateSubmit",form.validateSubmit)
                    // if( data.name_ ){
                    //     console.log(':::::::::::::::::KKKKKKKKKKKKK:::::::::::::')
                    // }
                    workflowState.value = data.workflow_state || '';
                },
                onError: (error) => {
                    console.error('Error:', error);
                    // alert(`An error occurred: ${error.message}`);
                }
            });
        });
        const handleFileChange=(event,field)=> {
            const file = event.target.files[0];
            
            if( field === 'addressProof' ){
                touched.addressProof = false;
            }

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
                    showToastMessage("File Upload Sucessfully")

                     // **Update form field here**
                    //  form[field] = file_url; 

                      // **Added code to hide validation message**
                    // if (field === 'addressProof') {
                    //     touched.addressProof = true;  //
                    // }

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
            if(form.validateSubmit){
                showErrorToastMessage("Please fill all mandatory details")
            }else{
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
                    setTimeout(() => {
                        location.reload();
                    }, 2000)
                },
                onError: (error) => {
                    console.error('Error:', error);
                    // alert(`An error occurred: ${error.message}`);
                }
            });
        }
        }
        function update(){
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.update_supplier_detail",
                makeParams: () => ({
                    doc: {
                        docname: form.docname,
                        workflow_state: "Change Request Pending with User"
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data)
                    // alert("Details Submitted Sucessfully")
                    showToastMessage("Details Update Sucessfully")
                    setTimeout(() => {
                        location.reload();
                    }, 2000)
                },
                onError: (error) => {
                    console.error('Error:', error);
                    // alert(`An error occurred: ${error.message}`);
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


        const showErrorToastMessage = (data) => {
            form.error = data
            showErrorToast.value = true;
            setTimeout(() => {
                showErrorToast.value = false;
            }, 1000);
        };
        const hideErrorToast = () => {
            showErrorToast.value = false;
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
            isValid,
            isReadonly,
            update,
            isupdate,
            showErrorToastMessage,
            hideErrorToast,
            showErrorToast
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

label {
    font-weight: 600;
}

h6 {
    color: #2e6bdc;
    font-weight: bolder;
}

/* tost css */

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