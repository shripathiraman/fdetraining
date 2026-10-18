export { };

const encounter = {
    encounterId: "12345",
    patient_nbr: 2022,
    patientName: "John Doe",
    age: "45",
    gender: "Male",
    risk_level: "High",
    status: "ASSIGNED"
};

const encounter1 = {
    encounterId: "123456",
    patient_nbr: 20223,
    patientName: "John Doe Shri",
    age: "45",
    gender: "Male",
    risk_level: "High",
    status: "ASSIGNED"
};

console.log(encounter);

const encounters = [encounter, encounter1];

console.log(encounters);