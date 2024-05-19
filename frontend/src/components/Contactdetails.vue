<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Contact Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="salutaion" class="form-label">Salutation</label>
                        <select name="salutaion" id="salutation" class="form-control" v-model="form.salutation">
                            <option value="Mr">Mr.</option>
                            <option value="Mrs">Mrs. </option>
                            <option value="Ms">Ms. </option>
                        </select>
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="firstName" v-model="form.firstName"
                            placeholder="First Name">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="lastName" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="lastName" v-model="form.lastName"
                            placeholder="Last Name">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="contact" class="form-label">Contact Number</label>
                        <input type="tel" maxlength="13" class="form-control" id="contact" v-model="form.contactNumber"
                            placeholder="Contact Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="email" class="form-label">Email ID</label>
                        <input type="email" class="form-control" id="email" v-model="form.emailId"
                            placeholder="Email Id">
                    </div>

                    <div class="col-md-4 mt-4 mb-3">
                        <input type="checkbox" v-model="form.markAsPrimary" id="markAsPrimary"
                            class="form-check-input mr-2">
                        <label for="markAsPrimary" class="form-check-label">Mark As Primary</label>
                    </div>
                </div>


                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Social Media Handlles</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Website</label>
                        <input type="text" class="form-control" id="Website" placeholder="Website">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Facebook</label>
                        <input type="text" class="form-control" id="Facebook" placeholder="Facebook">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">LinkedIn</label>
                        <input type="text" class="form-control" id="LinkedIn" placeholder="LinkedIn">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Instagram</label>
                        <input type="text" class="form-control" id="Instagram" placeholder="Instagram">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Twitter</label>
                        <input type="text" class="form-control" id="Twitter" placeholder="Twitter">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">YouTube</label>
                        <input type="text" class="form-control" id="YouTube" placeholder="YouTube">
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