import { useState } from 'react';
import SimInfo from '../SimInfo/SimInfo';
import FaceTemplates from '../FaceTemplates/FaceTemplates';
import Attributes from '../Attributes/Attributes';
import Modifiers from '../Modifiers/Modifiers';

const SimMain = () => {
	const [gender, setGender] = useState('');
	const [generateSim, setgenerateSim] = useState(false);

	const handleGender = (e) => {
		setGender(e.target.value);
	};

	const generateSimBtn = () => {
		setgenerateSim(true);
	};

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
								onChange={handleGender}
							/>
							<label htmlFor='male'>Male</label>
							<input
								type='radio'
								name='gender'
								id='female'
								value='female'
								onChange={handleGender}
							/>
							<label htmlFor='female'>Female</label>
						</div>
						<button onClick={generateSimBtn}>Generate Sim</button>
					</form>
				</div>
			</section>
			{/* Sim Info */}
			<SimInfo gender={gender} />
			{/* Face Templates */}
			<FaceTemplates gender={gender} />
			{/* Modifiers */}
			<Modifiers />
			{/* Attributes */}
			<Attributes gender={gender} />
		</>
	);
};
export default SimMain;
