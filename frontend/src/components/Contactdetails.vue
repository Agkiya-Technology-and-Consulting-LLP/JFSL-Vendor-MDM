<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Contact Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.salutation && !form.salutation }">
                        <label for="salutation" class="form-label">Salutation <span class="text-danger">*</span></label>
                        <select name="salutation" id="salutation" class="form-control" v-model="form.salutation" @blur="touched.salutation = true">
                            <option value=""></option>
                            <option value="Mr">Mr.</option>
                            <option value="Mrs">Mrs.</option>
                            <option value="Ms">Ms.</option>
                        </select>
                        <div v-if="touched.salutation && !form.salutation" class="text-danger">
                            Salutation is required.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.first_name && !form.first_name }">
                        <label for="firstName" class="form-label">First Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="firstName" v-model="form.first_name" placeholder="First Name" @blur="touched.first_name = true">
                        <div v-if="touched.first_name && !form.first_name" class="text-danger">
                            First Name is required.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.last_name && !form.last_name }">
                        <label for="lastName" class="form-label">Last Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="lastName" v-model="form.last_name" placeholder="Last Name" @blur="touched.last_name = true">
                        <div v-if="touched.last_name && !form.last_name" class="text-danger">
                            Last Name is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.contact_number && !form.contact_number }">
                        <label for="contact" class="form-label">Contact Number <span class="text-danger">*</span></label>
                        <input type="tel" maxlength="10" class="form-control" id="contact" v-model="form.contact_number" placeholder="Contact Number" @blur="touched.contact_number = true">
                        <div v-if="touched.contact_number && !form.contact_number" class="text-danger">
                            Contact Number is required.
                        </div>
                    </div>

                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.email_id && !form.email_id }">
                        <label for="email" class="form-label">Email ID <span class="text-danger">*</span></label>
                        <input type="email" class="form-control" id="email" v-model="form.email_id" placeholder="Email Id" @blur="touched.email_id = true">
                        <div v-if="touched.email_id && !form.email_id" class="text-danger">
                            Enter valid Email
                        </div>
                    </div>

                    <div class="col-md-4 mt-4 mb-3">
                        <input type="checkbox" v-model="form.mark_as_primary" id="markAsPrimary" class="form-check-input mr-2">
                        <label for="markAsPrimary" class="form-check-label">Mark As Primary</label>
                    </div>
                </div>

                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Social Media Handles</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="website" class="form-label">Website</label>
                        <input type="text" class="form-control" id="website" v-model="form.website" placeholder="Website">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="facebook" class="form-label">Facebook</label>
                        <input type="text" class="form-control" id="facebook" v-model="form.facebook" placeholder="Facebook">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="linkedin" class="form-label">LinkedIn</label>
                        <input type="text" class="form-control" id="linkedin" v-model="form.linkedin" placeholder="LinkedIn">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="instagram" class="form-label">Instagram</label>
                        <input type="text" class="form-control" id="instagram" v-model="form.instagram" placeholder="Instagram">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="twitter" class="form-label">Twitter</label>
                        <input type="text" class="form-control" id="twitter" v-model="form.twitter" placeholder="Twitter">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="youtube" class="form-label">YouTube</label>
                        <input type="text" class="form-control" id="youtube" v-model="form.youtube" placeholder="YouTube">
                    </div>
                </div>

                <div class="d-flex justify-content-end mt-1 mb-3">
                    <button type="button" class="savebutton" @click="ValidateEmail" :disabled="!isValid">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, defineComponent, onMounted, reactive, computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';

export default defineComponent({
    name: 'ContactDetails',
    setup() {
        const form = reactive({
            salutation: '',
            first_name: '',
            last_name: '',
            contact_number: '',
            email_id: '',
            mark_as_primary: false,
            docname: '',
            website: '',
            facebook: '',
            linkedin: '',
            instagram: '',
            twitter: '',
            youtube: ''
        });

        const touched = reactive({
            salutation: false,
            first_name: false,
            last_name: false,
            contact_number: false,
            email_id: false
        });

        const loginUser = sessionUser();

        const isValid = computed(() => {
            return form.salutation && form.first_name && form.last_name && form.contact_number && form.email_id;
        });

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
                    form.first_name = data.first_name || '';
                    form.salutation = data.salutation || '';
                    form.last_name = data.last_name || '';
                    form.contact_number = data.contact_number || '';
                    form.email_id = data.email_id || '';
                    form.mark_as_primary = data.mark_as_primary || true;
                    form.website = data.website || '';
                    form.facebook = data.facebook || '';
                    form.linkedin = data.linkedin || '';
                    form.instagram = data.instagram || '';
                    form.twitter = data.twitter || '';
                    form.youtube = data.youtube || '';
                    form.docname = data.name || '';
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });

        const ValidateEmail = () => {
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        salutation: form.salutation,
                        first_name: form.first_name,
                        last_name: form.last_name,
                        contact_number: form.contact_number,
                        email_id: form.email_id,
                        mark_as_primary: form.mark_as_primary,
                        docname: form.docname,
                        website: form.website,
                        facebook: form.facebook,
                        linkedin: form.linkedin,
                        instagram: form.instagram,
                        twitter: form.twitter,
                        youtube: form.youtube
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data);
                    alert("Details Saved Sucessfully")
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
        };

        return {
            form,
            touched,
            isValid,
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
    padding: 0px 20px 0px 20px;
    border-radius: 10px;
}

label {
    font-weight: 600;
}

h5 {
    color: #fff;
    font-weight: bolder;
}

.text-danger {
    color: red;
}

.has-error input,
.has-error select {
    border-color: red;
}

/* .has-error label {
    color: red;
} */
:disabled{
    background-color: grey;
    cursor:not-allowed;
}
</style>
