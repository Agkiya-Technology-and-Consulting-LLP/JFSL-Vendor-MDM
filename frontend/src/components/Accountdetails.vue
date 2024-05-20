<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">

                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Account Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Account Number" class="form-label">Account Number</label>
                        <input type="text" class="form-control" id="Account Number" v-model="form.account_number" placeholder="Account Number">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="Confirm Account Number" class="form-label">Confirm Account Number</label>
                        <input type="text" class="form-control" id="Confirm Account Number" v-model="form.confirm_account_number"
                            placeholder="Confirm Account Number">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="IFSC Code" class="form-label">IFSC Code</label>
                        <input type="text" class="form-control" id="IFSC Code" v-model="form.ifsc_code"
                            placeholder="IFSC Code">
                    </div>
                </div>

                <div class="row mt-3">

                    <div class="col-md-4 mb-3">
                        <label for="Name Of Bank" class="form-label">Name Of Bank</label>
                        <input type="text" class="form-control" id="Name Of Bank" v-model="form.name_of_bank" placeholder="Name Of Bank">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Branch Contact number" class="form-label">Branch Contact number</label>
                        <input type="tel" maxlength="13" class="form-control" id="contact" v-model="form.branch_contact_number"
                            placeholder="Contact Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Branch Email Id" class="form-check-label">Branch Email Id</label>
                        <input type="text" class="form-control" id="Branch Email Id" v-model="form.branch_email_id" placeholder="Branch Email Id">
                    </div>
                </div>


                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Bank Address</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Bank Address" class="form-label">Bank Address</label>
                        <input type="text" class="form-control" id="Bank Address" v-model="form.bank_address" placeholder="Bank Address">
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
                        <input type="tel" maxlength="13" class="form-control"  id="Zipcode" v-model="form.branch_zipcode"
                            placeholder="Zipcode">
                    </div>
                </div>


                <div class="d-flex justify-content-end mt-1 mb-3">
                    <Button type="button" class="savebutton" @click="ValidateEmail()">Save</Button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, defineComponent, onMounted, reactive } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';



export default defineComponent({
    name: 'ContactDetails',
    setup() {
        const form = reactive({
            account_number: '',
            confirm_account_number: '',
            ifsc_code: '',
            name_of_bank: '',
            branch_contact_number: '',
            docname:'',
            branch_email_id:'',
            bank_address:'',
            branch_country:'',
            branch_state:'',
            branch_city:'',
            branch_zipcode:''
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
                    console.log(data);
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
                    form.docname=data.name
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });

        const ValidateEmail = () => {
            console.log('values are here', form);
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        account_number: form.account_number,
                        confirm_account_number: form.confirm_account_number,
                        ifsc_code: form.ifsc_code,
                        contact_number: form.contact_number,
                        name_of_bank: form.name_of_bank,
                        docname:form.docname,
                        branch_contact_number:form.branch_contact_number,
                        branch_email_id:form.branch_email_id,
                        bank_address:form.bank_address,
                        branch_country:form.branch_country,
                        branch_state:form.branch_state,
                        branch_city :form.branch_city,
                        branch_zipcode : form.branch_zipcode
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

        };

        return {
            form,
            ValidateEmail
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
</style>