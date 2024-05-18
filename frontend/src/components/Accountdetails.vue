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
                        <input type="text" class="form-control" id="Account Number" placeholder="Account Number">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="Confirm Account Number" class="form-label">Confirm Account Number</label>
                        <input type="text" class="form-control" id="Confirm Account Number"
                            placeholder="Confirm Account Number">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="IFSC Code" class="form-label">IFSC Code</label>
                        <input type="text" class="form-control" id="IFSC Code" 
                            placeholder="IFSC Code">
                    </div>
                </div>

                <div class="row mt-3">

                    <div class="col-md-4 mb-3">
                        <label for="Name Of Bank" class="form-label">Name Of Bank</label>
                        <input type="text" class="form-control" id="Name Of Bank" placeholder="Name Of Bank">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Branch Contact number" class="form-label">Branch Contact number</label>
                        <input type="tel" maxlength="13" class="form-control" id="contact" v-model="form.contactNumber"
                            placeholder="Contact Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="Branch Email Id" class="form-check-label">Branch Email Id</label>
                        <input type="text" class="form-control" id="Branch Email Id" placeholder="Branch Email Id">
                    </div>
                </div>


                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Bank Address</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="Bank Address" class="form-label">Bank Address</label>
                        <input type="text" class="form-control" id="Bank Address" placeholder="Bank Address">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="Country" class="form-label">Country</label>
                        <input type="text" class="form-control" id="Country"
                            placeholder="Country">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="State" class="form-label">State</label>
                        <input type="text" class="form-control" id="State" 
                            placeholder="State">
                    </div>
                </div>

                <div class="row mt-3">

                    <div class="col-md-6 mb-3">
                        <label for="City" class="form-label">City</label>
                        <input type="text" class="form-control" id="City" placeholder="City">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="Zipcode" class="form-label">Zipcode</label>
                        <input type="tel" maxlength="13" class="form-control" id="Zipcode" v-model="form.contactNumber"
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
export default {
    name: 'ContactDetails',
    data() {
        return {
            form: {
                salutation: '',
                firstName: '',
                lastName: '',
                contactNumber: '',
                emailId: '',
                markAsPrimary: true,
            }
        }
    },
    methods: {
        ValidateEmail() {
            console.log('values is here', this.form);
        },
    }
};
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