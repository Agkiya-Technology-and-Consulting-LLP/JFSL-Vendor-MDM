<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-1 rounded-top">
                    <h5>Supplier Details</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.supplier_name && !form.supplier_name }">
                        <label for="supplierName" class="form-label">Supplier Name <span class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="supplierName" v-model="form.supplier_name"
                            placeholder="Supplier Name" @blur="touched.supplier_name = true" :readonly="isReadonly">
                        <div v-if="touched.supplier_name && !form.supplier_name" class="text-danger">
                            Supplier Name is required.
                        </div>
                    </div>
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.supplier_type && !form.supplier_type }">
                        <label for="supplierType" class="form-label">Supplier Type <span class="text-danger">*</span></label>
                        <select name="supplierType" id="supplierType" class="form-control" v-model="form.supplier_type" @blur="touched.supplier_type = true" :disabled="isReadonly">
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
                        <div v-if="touched.supplier_type && !form.supplier_type" class="text-danger">
                            Supplier Type is required.
                        </div>
                    </div>
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.related_party && !form.related_party }">
                        <label for="relatedParty" class="form-label">Related Party <span class="text-danger">*</span></label>
                        <select name="relatedParty" id="relatedParty" class="form-control" v-model="form.related_party" @blur="touched.related_party = true">
                            <option value=""></option>
                            <option value="No">No</option>
                            <option value="Yes">Yes </option>
                        </select>
                        <div v-if="touched.related_party && !form.related_party" class="text-danger">
                            Related Party is required.
                        </div>
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-4 mb-3" :class="{ 'has-error': touched.supplier_details && !form.supplier_details }">
                        <label for="supplierDetails" class="form-label">Supplier Details <span class="text-danger">*</span></label>
                        <textarea maxlength="1000" class="form-control" id="supplierDetails" v-model="form.supplier_details" @blur="touched.supplier_details = true"></textarea>
                        <div v-if="touched.supplier_details && !form.supplier_details" class="text-danger">
                            Supplier Details is required.
                        </div>
                    </div>
                </div>

                <div class="d-flex justify-content-end gap-2 mt-1 mb-3">
                    <button type="button" class="savebutton" @click="ValidateEmail" :disabled="!isValid">Save</button>
                    <router-link to="/contactdetails"><button class="nextbutton">Next</button></router-link>
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
          Details Saved Sucessfully.
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
import { ref, defineComponent, onMounted, reactive, computed } from "vue";
import { sessionUser } from "../data/session";
import { createResource } from 'frappe-ui';
const showToast = ref(false);
const isReadonly = ref(false);


export default defineComponent({
    name: 'ContactDetails',
    setup() {
        const form = reactive({
            supplier_name: '',
            supplier_type: '',
            related_party: '',
            supplier_details: '',
            docname: ''
        });

        const touched = reactive({
            supplier_name: false,
            supplier_type: false,
            related_party: false,
            supplier_details: false
        });

        const loginUser = sessionUser();

        const isValid = computed(() => {
            return form.supplier_name && form.supplier_type && form.related_party && form.supplier_details;
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
                        form.supplier_name = data.supplier_name || '';
                        form.supplier_type = data.supplier_type || '';
                        form.related_party = data.related_party || '';
                        form.supplier_details = data.supplier_details || '';
                        form.docname = data.name;
                        console.log(form.docname)

                        isReadonly.value = !!data.supplier_name; 
                },
                onError: (error) => {
                    console.error('Error:', error);
                }
            });
        });

        function ValidateEmail() {
            const supplier = createResource({
                url: "jsfl_vendor_mdm.jsfl_vendor_mdm.custom.api.save_supplier_detail",
                makeParams: () => ({
                    doc: {
                        supplier_name: form.supplier_name,
                        supplier_type: form.supplier_type,
                        related_party: form.related_party,
                        supplier_details: form.supplier_details,
                        docname: form.docname
                    }
                }),
                auto: true,
                onSuccess: (data) => {
                    console.log(data);
                    showToastMessage()
                    isReadonly.value = true;
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
            touched,
            isValid,
            ValidateEmail,
            hideToast,
            showToastMessage,
            showToast,
            isReadonly
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

h6 {
    color: #2e6bdc;
    font-weight: bolder;
}

.text-danger {
    color: red;
}

.has-error input, .has-error select, .has-error textarea {
    border-color: red;
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
    font-size: 1.5rem;
    padding: 0px 20px 0px 20px;
    border-radius: 10px;
}
</style>
