interface PatientEncounter {
    encounterId: string;
    patient_nbr: number;
    patientName: string;
    age: string;
    gender: string;
    risk_level: string;
    status: string;
}

const encounter: PatientEncounter = {
    encounterId: "12345",
    patient_nbr: 2022,
    patientName: "John Doe",
    age: "45",
    gender: "Male",
    risk_level: "High",
    status: "ASSIGNED"
};

const encounters: PatientEncounter[] = [encounter];

encounters.push({
    encounterId: "123456",
    patient_nbr: 20223,
    patientName: "John Doe Shri",
    age: "45",
    gender: "Male",
    risk_level: "High",
    status: "ASSIGNED"
})

console.log(encounters);