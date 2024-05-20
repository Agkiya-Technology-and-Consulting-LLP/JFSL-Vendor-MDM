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
                        <input type="text" class="form-control" id="firstName" v-model="form.first_name"
                            placeholder="First Name">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="lastName" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="lastName" v-model="form.last_name"
                            placeholder="Last Name">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="contact" class="form-label">Contact Number</label>
                        <input type="tel" maxlength="13" class="form-control" id="contact" v-model="form.contact_number"
                            placeholder="Contact Number">
                    </div>

                    <div class="col-md-4 mb-3">
                        <label for="email" class="form-label">Email ID</label>
                        <input type="email" class="form-control" id="email" v-model="form.email_id"
                            placeholder="Email Id">
                    </div>

                    <div class="col-md-4 mt-4 mb-3">
                        <input type="checkbox" v-model="form.mark_as_primary" id="markAsPrimary"
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
                        <input type="text" class="form-control" id="Website" v-model="form.website" placeholder="Website">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Facebook</label>
                        <input type="text" class="form-control" id="Facebook"  v-model="form.facebook" placeholder="Facebook">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">LinkedIn</label>
                        <input type="text" class="form-control" id="LinkedIn" v-model="form.linkedin" placeholder="Linkedin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Instagram</label>
                        <input type="text" class="form-control" id="Instagram" v-model="form.instagram" placeholder="Instagram">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Twitter</label>
                        <input type="text" class="form-control" id="Twitter" v-model="form.twitter" placeholder="Twitter">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">YouTube</label>
                        <input type="text" class="form-control" id="YouTube" v-model="form.youtube" placeholder="Youtube">
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
            salutation: '',
            first_name: '',
            last_name: '',
            contact_number: '',
            email_id: '',
            mark_as_primary: true,
            docname:'',
            website:'',
            facebook:'',
            linkedin:'',
            instagram:'',
            twitter:'',
            youtube:''
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
                    form.first_name = data.first_name;
                    form.salutation = data.salutation;
                    form.last_name = data.last_name;
                    form.contact_number = data.contact_number;
                    form.email_id = data.email_id;
                    form.mark_as_primary = data.mark_as_primary;
                    form.website = data.website;
                    form.facebook = data.facebook;
                    form.linkedin = data.linkedin;
                    form.instagram = data.instagram;
                    form.twitter = data.twitter;
                    form.youtube = data.youtube;
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
                        first_name: form.first_name,
                        salutation: form.salutation,
                        last_name: form.last_name,
                        email_id: form.email_id,
                        mark_as_primary: form.mark_as_primary,
                        docname:form.docname,
                        website:form.website,
                        facebook:form.facebook,
                        linkedin:form.linkedin,
                        instagram:form.instagram,
                        twitter:form.twitter,
                        youtube :form.youtube
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