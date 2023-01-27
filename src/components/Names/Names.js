import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
	faMars,
	faVenus,
	faDog,
	faCat,
} from '@fortawesome/free-solid-svg-icons';

import './names.css';

const Names = () => {
	return (
		<>
			{/* Choose 1 random name for Sim */}
			<div className='random__name--sim'>
				<h2>Choose a gender for a sim name</h2>
				<form>
					<div className='gender__selection'>
						<div className='gender__selection--choice'>
							<label htmlFor='male' title='Male'>
								<FontAwesomeIcon className='gender__icon' icon={faMars} />
							</label>
							<input type='radio' name='gender' id='male' value='male' />
						</div>
						<div className='gender__selection--choice'>
							<input type='radio' name='gender' id='female' value='female' />
							<label htmlFor='female' title='Female'>
								<FontAwesomeIcon className='gender__icon' icon={faVenus} />
							</label>
						</div>
					</div>
					<button>Get a random name!</button>
				</form>
			</div>

			{/* Display random name for sim */}
			<div className='random__name--answer'>
				<p className='random__name--name'>Hayley</p>
			</div>

			<hr />

			{/* Search for a name for Sim */}
			<div className='search__name--sim'>
				<h2>Choose name for sim based on conditions</h2>
				<form>
					<div className='gender__selection'>
						<div className='gender__selection--choice'>
							<label htmlFor='male' title='Male'>
								<FontAwesomeIcon className='gender__icon' icon={faMars} />
							</label>
							<input type='radio' name='gender' id='male' value='male' />
						</div>
						<div className='gender__selection--choice'>
							<input type='radio' name='gender' id='female' value='female' />
							<label htmlFor='female' title='Female'>
								<FontAwesomeIcon className='gender__icon' icon={faVenus} />
							</label>
						</div>
					</div>
					<div className='form__selection'>
						<label htmlFor='numOfNames'>Number of Names: </label>
						<input type='number' min='1' max='10' size='1' id='numOfNames' />
					</div>
					<div className='form__selection'>
						<label htmlFor='nameLetter'>Names beginning with: </label>
						<input type='text' maxLength='1' size='1' id='nameLetter' />
					</div>
					<button>Get list of Names</button>
				</form>
			</div>

			{/* Display list of names for sims */}
			<div className='search__name--results'>
				<h2>Results:</h2>
				<ul className='search__name--list'>
					<li className='search__name--listitem'>Hayley</li>
					<li className='search__name--listitem'>Hannah</li>
					<li className='search__name--listitem'>Hazel</li>
					<li className='search__name--listitem'>Harriet</li>
				</ul>
			</div>

			<hr />

			{/* Choose 1 random name for Pet */}
			<div className='random__name--pet'>
				<h2>Choose type of pet and gender for a pet name</h2>
				<form>
					<div className='pet__selection'>
						<div className='pet__selection--choice'>
							<label htmlFor='dog' title='Dog'>
								<FontAwesomeIcon className='pet__icon' icon={faDog} />
							</label>
							<input type='radio' name='pet' id='dog' value='dog' />
						</div>
						<div className='pet__selection--choice'>
							<input type='radio' name='pet' id='cat' value='cat' />
							<label htmlFor='cat' title='Cat'>
								<FontAwesomeIcon className='pet__icon' icon={faCat} />
							</label>
						</div>
					</div>
					<div className='gender__selection'>
						<div className='gender__selection--choice'>
							<label htmlFor='male' title='Male'>
								<FontAwesomeIcon className='gender__icon' icon={faMars} />
							</label>
							<input type='radio' name='gender' id='male' value='male' />
						</div>
						<div className='gender__selection--choice'>
							<input type='radio' name='gender' id='female' value='female' />
							<label htmlFor='female' title='Female'>
								<FontAwesomeIcon className='gender__icon' icon={faVenus} />
							</label>
						</div>
					</div>
					<button>Get a random name!</button>
				</form>
			</div>

			{/* Display random name for pet */}
			<div className='random__name--answer'>
				<p className='random__name--name'>Hayley</p>
			</div>

			<hr />
			{/* Search for a name for Pet */}
			<div className='search__name--sim'>
				<h2>Choose name for sim based on conditions</h2>
				<form>
					<div className='pet__selection'>
						<div className='pet__selection--choice'>
							<label htmlFor='dog' title='Dog'>
								<FontAwesomeIcon className='pet__icon' icon={faDog} />
							</label>
							<input type='radio' name='pet' id='dog' value='dog' />
						</div>
						<div className='pet__selection--choice'>
							<input type='radio' name='pet' id='cat' value='cat' />
							<label htmlFor='cat' title='Cat'>
								<FontAwesomeIcon className='pet__icon' icon={faCat} />
							</label>
						</div>
					</div>
					<div className='gender__selection'>
						<div className='gender__selection--choice'>
							<label htmlFor='male' title='Male'>
								<FontAwesomeIcon className='gender__icon' icon={faMars} />
							</label>
							<input type='radio' name='gender' id='male' value='male' />
						</div>
						<div className='gender__selection--choice'>
							<input type='radio' name='gender' id='female' value='female' />
							<label htmlFor='female' title='Female'>
								<FontAwesomeIcon className='gender__icon' icon={faVenus} />
							</label>
						</div>
					</div>
					<div className='form__selection'>
						<label htmlFor='numOfNames'>Number of Names: </label>
						<input type='number' min='1' max='10' size='1' id='numOfNames' />
					</div>
					<div className='form__selection'>
						<label htmlFor='nameLetter'>Names beginning with: </label>
						<input type='text' maxLength='1' size='1' id='nameLetter' />
					</div>
					<button>Get list of Names</button>
				</form>
			</div>

			{/* Display list of names for pets */}
			<div className='search__name--results'>
				<h2>Results:</h2>
				<ul className='search__name--list'>
					<li className='search__name--listitem'>Hayley</li>
					<li className='search__name--listitem'>Hannah</li>
					<li className='search__name--listitem'>Hazel</li>
					<li className='search__name--listitem'>Harriet</li>
				</ul>
			</div>
		</>
	);
};
export default Names;
