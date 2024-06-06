<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">

                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Account Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.account_number && !form.account_number }">
                        <label for="AccountNumber" class="form-label">Account Number <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="AccountNumber" v-model="form.account_number"
                            placeholder="Account Number" @blur="touched.account_number = true">
                        <div v-if="touched.account_number && !form.account_number" class="text-danger">
                            Account Number is required.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3"
                        :class="{ 'has-error': touched.confirm_account_number && !form.confirm_account_number }">
                        <label for="ConfirmAccountNumber" class="form-label">Confirm Account Number <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="ConfirmAccountNumber"
                            v-model="form.confirm_account_number" placeholder="Confirm Account Number"
                            @blur="touched.confirm_account_number = true">
                        <div v-if="touched.confirm_account_number && !form.confirm_account_number" class="text-danger">
                            Confirm Account Number is required.
                        </div>
                        <div v-if="match" class="text-danger">
                            Enter correct account number.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.ifsc_code && !form.ifsc_code }">
                        <label for="IFSCCode" class="form-label">IFSC Code <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="IFSCCode" v-model="form.ifsc_code"
                            placeholder="IFSC Code" @blur="touched.ifsc_code = true">
                        <div v-if="touched.ifsc_code && !form.ifsc_code" class="text-danger">
                            IFSC Code is required.
                        </div>
                    </div>

                </div>

                <div class="row mt-3">

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.name_of_bank && !form.name_of_bank }">
                        <label for="NameOfBank" class="form-label">Name Of Bank <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="NameOfBank" v-model="form.name_of_bank"
                            placeholder="Name Of Bank" @blur="touched.name_of_bank = true">
                        <div v-if="touched.name_of_bank && !form.name_of_bank" class="text-danger">
                            Name Of Bank is required.
                        </div>
                    </div>


                    <div class="col-md-4 mb-3">
                        <label for="Branch Contact number" class="form-label">Branch Contact number</label>
                        <input type="tel" maxlength="13" class="form-control" id="contact"
                            v-model="form.branch_contact_number" placeholder="Contact Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Branch Email Id" class="form-check-label">Branch Email Id</label>
                        <input type="text" class="form-control" id="Branch Email Id" v-model="form.branch_email_id"
                            placeholder="Branch Email Id">
                    </div>
                </div>


                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Bank Address</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Bank Address" class="form-label">Bank Address</label>
                        <input type="text" class="form-control" id="Bank Address" v-model="form.bank_address"
                            placeholder="Bank Address">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="Country" class="form-label">Country</label>
                        <input type="text" class="form-control" id="Country" v-model="form.branch_country"
                            placeholder="Country">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="State" class="form-label">State</label>
                        <input type="text" class="form-control" id="State" v-model="form.branch_state"
                            placeholder="State">
                    </div>
                </div>

                <div class="row mt-3">

                    <div class="col-md-6 mb-3">
                        <label for="City" class="form-label">City</label>
                        <input type="text" class="form-control" id="City" v-model="form.branch_city" placeholder="City">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="Zipcode" class="form-label">Zipcode</label>
                        <input type="tel" maxlength="13" class="form-control" id="Zipcode" v-model="form.branch_zipcode"
                            placeholder="Zipcode">
                    </div>
                </div>


                <div class="d-flex justify-content-end gap-2 mt-1 mb-3">
                    <Button type="button" class="savebutton" @click="ValidateEmail()" :disabled="!isValid">Save</Button>
                    <router-link to="/documentdetails" class="nextbutton"><button>Next</button></router-link>
                </div>
            </div>
        </div>
    </div>
    <!-- Tost Message -->
    <div class="toast align-items-center text-white bg-success  border-0" role="alert" aria-live="assertive"
        aria-atomic="true" :class="{ 'show': showToast }">
        <div class="d-flex">
            <div class="toast-body">
                Details Saved Sucessfully.
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
import { ref, defineComponent, onMounted, reactive, watch, computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);
const match =ref(false)
const showErrorToast = ref(false)
export default defineComponent({
    name: 'ContactDetails',
    setup() {
        const form = reactive({
            account_number: '',
            confirm_account_number: '',
            ifsc_code: '',
            name_of_bank: '',
            branch_contact_number: '',
            docname: '',
            branch_email_id: '',
            bank_address: '',
            branch_country: '',
            branch_state: '',
            branch_city: '',
            branch_zipcode: '',
        });

        const touched = reactive({
            account_number: false,
            confirm_account_number: false,
            ifsc_code: false,
            name_of_bank: false,
        });
        const isValid = computed(() => {
            return form.account_number && form.confirm_account_number && form.confirm_account_number && form.name_of_bank;
        });

        const loginUser = sessionUser();

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
                    form.account_number = data.account_number;
                    form.confirm_account_number = data.confirm_account_number;
                    form.ifsc_code = data.ifsc_code;
                    form.contact_number = data.contact_number;
                    form.name_of_bank = data.name_of_bank;
                    form.branch_contact_number = data.branch_contact_number;
                    form.branch_email_id = data.branch_email_id;
                    form.bank_address = data.bank_address;
                    form.branch_country = data.branch_country;
                    form.branch_state = data.branch_state;
                    form.branch_city = data.branch_city;
                    form.branch_zipcode = data.branch_zipcode;
                    form.docname = data.name
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });

        const ValidateEmail = () => {
            if(match.value ==true){
                showErrorToastMessage("Enter correct Account No.")
            }else{
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        account_number: form.account_number,
                        confirm_account_number: form.confirm_account_number,
                        ifsc_code: form.ifsc_code,
                        contact_number: form.contact_number,
                        name_of_bank: form.name_of_bank,
                        docname: form.docname,
                        branch_contact_number: form.branch_contact_number,
                        branch_email_id: form.branch_email_id,
                        bank_address: form.bank_address,
                        branch_country: form.branch_country,
                        branch_state: form.branch_state,
                        branch_city: form.branch_city,
                        branch_zipcode: form.branch_zipcode
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    showToastMessage()
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
        }
        };
        watch(() => form.ifsc_code,
            (newValue, oldValue) => {
                if (oldValue && newValue != oldValue) {
                    try {
                        const response = createResource({
                            url: 'jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.get_bank_details',
                            makeParams: () => ({
                                data: {
                                    ifscCode: newValue
                                },
                            }),
                            auto: true,
                            onSuccess: (data) => {
                                form.name_of_bank = data.result.bank;
                                form.bank_address = data.result.address;
                                form.branch_state = data.result.state
                                form.branch_city = data.result.city
                                form.branch_contact_number = data.result.contact

                            }, onError: (error) => {
                                console.log(error)
                            }
                        });

                    } catch (error) {
                        console.error('Error fetching bank details:', error);
                    }
                }


            })


        watch(()=>form.confirm_account_number,
        (value)=>{
            if(form.account_number != form.confirm_account_number){
                match.value =true
            }else{
                match.value =false
            }
            
        })
        const showToastMessage = () => {
            showToast.value = true;
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
            hideToast,
            showToastMessage,
            hideErrorToast,
            showErrorToast,
            showToast,
            match,
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
    height: 2rem;
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
.nextbutton{
    background-color: #2e6bdc;
    color: white;
    font-size: 1.20rem;
    padding: 0px 20px 0px 20px;
    border-radius: 10px;
}
</style>