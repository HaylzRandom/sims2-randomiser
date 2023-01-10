import { useState } from 'react';
import SimInfo from '../SimInfo/SimInfo';
import FaceTemplates from '../FaceTemplates/FaceTemplates';
import Attributes from '../Attributes/Attributes';
import Modifiers from '../Modifiers/Modifiers';


const SimMain = () => {
	const [gender, setGender] = useState('');
	const [generateSim, setgenerateSim] = useState(false);

	const generateSimBtn = (e) => {
		e.preventDefault();
		setgenerateSim(!generateSim);
	};

	const content = (
		<>
			<SimInfo gender={gender} generateSim={generateSim} />
			<FaceTemplates gender={gender} />
			<Modifiers />
			<Attributes generateSim={generateSim} />
		</>
	);

	return (
		<>
			{/* Sim Gender Selector */}
			<section id='sim__gender'>
				<div className='sim__gender--select'>
					<form>
						<div className='gender__selection'>
							<input
								type='radio'
								name='gender'
								id='male'
								value='male'
								onChange={(e) => setGender(e.target.value)}
							/>
							<label htmlFor='male'>Male</label>
							<input
								type='radio'
								name='gender'
								id='female'
								value='female'
								onChange={(e) => setGender(e.target.value)}
							/>
							<label htmlFor='female'>Female</label>
						</div>
						<button onClick={generateSimBtn}>Generate Sim</button>
					</form>
				</div>
			</section>

			{generateSim && content}

			<button onClick={generateSimBtn}>Reset</button>
		</>
	);
};
export default SimMain;
