<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="bg-primary text-white p-2 rounded-top">
                    <h5>Documents</h5>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="Address Proof" class="form-label">Address Proof</label>
                        <input type="file" class="form-control" id="Address Proof" v-on:change="form.addressProof">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="MSMED/Udyam Registration" class="form-label">MSMED/Udyam Registration</label>
                        <input type="file" class="form-control" id="MSMED/Udyam Registration"
                            v-on:change="form.msmedUdyamNumber">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PAN/Aadhar" class="form-label">PAN/Aadhar</label>
                        <input type="file" class="form-control" id="PAN/Aadhar" v-on:change="form.panAadhar">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="ESIC" class="form-label">ESIC</label>
                        <input type="file" class="form-control" id="ESIC" v-on:change="form.esic">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="PF" class="form-label">PF</label>
                        <input type="file" class="form-control" id="PF" v-on:change="form.pf">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="TIN/UIN" class="form-label">TIN/UIN</label>
                        <input type="file" class="form-control" id="TIN/UIN" v-on:change="form.tinUin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="GST" class="form-label">GST</label>
                        <input type="file" class="form-control" id="GST" v-on:change="form.gst">
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="CIN" class="form-label">CIN</label>
                        <input type="file" class="form-control" id="CIN" v-on:change="form.cin">
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6 mb-3">
                        <label for="LST/CST" class="form-label">LST/CST</label>
                        <input type="file" class="form-control" id="LST/CST" v-on:change="form.lstCst">
                    </div>
                </div>

                <div class="d-flex justify-content-end mt-1 mb-3">
                <Button type="button" class="savebutton">Save</Button>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Documents',
    data() {
        return {
            form: {
                addressProof: '',
                msmedUdyamNumber: '',
                panAadhar: '',
                esic: '',
                pf: '',
                tinUin: '',
                gst: '',
                cin: '',
                lstCst: '',
            }
        }
    },
};
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
label{
    font-weight:600;
}
h6{
    color: #2e6bdc;
    font-weight: bolder;
}
</style>