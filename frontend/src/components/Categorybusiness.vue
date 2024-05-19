<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Supplier Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="firstName" class="form-label">Supplier Name</label>
                        <input type="text" class="form-control" id="firstName" v-model="form.supplier_name"
                            placeholder="Supplier Name">
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="salutaion" class="form-label">Supplier Type</label>
                        <select name="salutaion" id="salutation" class="form-control" v-model="form.supplier_type" >
                            <option value=""></option>
                            <option value="Company">Company</option>
                            <option value="Individual">Individual </option>
                            <option value="Firm">Firm </option>
                            <option value="Hindu Undivided Family">Hindu Undivided Family </option>
                            <option value="TRUST">TRUST </option>
                            <option value="Body of Individuals">Body of Individuals </option>
                            <option value="Association of persons">Association of persons </option>
                            <option value="Artificial Juridical Person">Artificial Juridical Person </option>
                            <option value="Local Authority">Local Authority </option>
                            <option value="Government">Government </option>
                            <option value="Non PAN">Non PAN </option>
                            
                        </select>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label for="salutaion" class="form-label">Related Party</label>
                        <select name="salutaion" id="salutation" class="form-control" v-model="form.related_party">
                            <option value="No">No</option>
                            <option value="Yes">Yes </option>
                        </select>
                    </div>

    
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3">
                        <label for="contact" class="form-label">Supplier Details</label>
                        <textarea maxlength="1000" class="form-control" id="contact" v-model="form.supplier_details"></textarea>

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
            supplier_name: '',
            supplier_type: '',
            related_party: '',
            supplier_details: '',
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
                    if (data && data.supplier_name !== undefined) {
                        console.log(data);
                        form.supplier_name = data.supplier_name || '';
                        form.supplier_type = data.supplier_type || '';
                        form.related_party = data.related_party || '';
                        form.supplier_details = data.supplier_details || '';
                        form.docname=data.name
                    } else {
                        console.log("Received data is not in expected format", data);
                    }
                },
                onError: (error) => {
                    console.error('Error:', error);
                    alert(`An error occurred: ${error.message}`);
                }
            });
        });

        function ValidateEmail() {
            console.log('values are here', form);
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        supplier_name: form.supplier_name,
                        supplier_type: form.supplier_type,
                        related_party: form.related_party,
                        supplier_details: form.supplier_details,
                        docname:form.docname
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
        }

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
label{
    font-weight:600;
}
h6{
    color: #2e6bdc;
    font-weight: bolder;
}
</style>